# GitHub Setup Instructions for SoftConnect

This guide will help you set up your GitHub repository and configure automatic builds for SoftConnect.

## Step 1: Create a New GitHub Repository

1. Go to https://github.com and log in
2. Click the "+" icon in the top right and select "New repository"
3. Name your repository (e.g., "softconnect")
4. Choose "Private" or "Public" depending on your needs
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

## Step 2: Push Your Code to GitHub

After creating the repository, run these commands in your terminal:

```bash
cd /Users/davuddemic/Repositories/rustdesk

# Add your new GitHub repository as the remote
git remote add origin https://github.com/YOUR_USERNAME/softconnect.git

# Push the code to GitHub
git push -u origin master

# Push the submodule changes
git submodule foreach git push origin HEAD:refs/heads/soft1-branding
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 3: Enable GitHub Actions

GitHub Actions should be automatically enabled for your repository. The RustDesk project already includes workflow files that will:

- Build Windows installers (x64)
- Build macOS apps (Intel + Apple Silicon)
- Build Linux packages (AppImage, deb, rpm)
- Build Android APK
- Build iOS app (requires signing)

### Check Workflow Status

1. Go to your repository on GitHub
2. Click the "Actions" tab
3. You should see builds starting automatically

## Step 4: Configure Build Secrets (Optional)

For code signing and releases, you may need to add secrets:

1. Go to your repository settings
2. Click "Secrets and variables" → "Actions"
3. Add secrets as needed:
   - `APPLE_CERTIFICATE` - For macOS code signing
   - `APPLE_PASSWORD` - For notarization
   - `ANDROID_KEYSTORE` - For Android signing
   - `WINDOWS_CERTIFICATE` - For Windows code signing

## Step 5: Download Built Installers

Once the GitHub Actions workflows complete:

1. Go to the "Actions" tab
2. Click on a completed workflow run
3. Scroll down to "Artifacts"
4. Download the installers for your desired platforms:
   - `SoftConnect-Windows-x64.exe`
   - `SoftConnect-macOS.dmg`
   - `SoftConnect-Linux.AppImage`
   - `SoftConnect-Android.apk`
   - etc.

## Alternative: Manual Builds

If you prefer to build manually or need to test locally:

### Prerequisites

Install required dependencies:
- Rust toolchain: https://rustup.rs/
- Flutter SDK: https://flutter.dev/docs/get-started/install
- Platform-specific SDKs (Xcode for macOS/iOS, Android Studio for Android, etc.)

### Build Commands

**Desktop (Windows/macOS/Linux):**
```bash
cd /Users/davuddemic/Repositories/rustdesk
python3 build.py --flutter --release
```

**Android:**
```bash
cd /Users/davuddemic/Repositories/rustdesk/flutter
flutter build apk --release
```

**iOS:**
```bash
cd /Users/davuddemic/Repositories/rustdesk/flutter
flutter build ios --release
```

## Troubleshooting

### Submodule Issues

If you encounter submodule errors:
```bash
git submodule update --init --recursive
```

### Build Failures

1. Check the GitHub Actions logs for specific errors
2. Ensure all dependencies are properly installed
3. Verify that the server `remote.soft1.ch` is accessible and running

### Icon Issues

- Windows ICO files need to be created manually (see BRANDING.md)
- Android and iOS icons need to be generated in multiple sizes (see BRANDING.md)

## Next Steps

1. **Test the builds** thoroughly on all target platforms
2. **Update help documentation** in the app to reference soft1.ch
3. **Set up automatic updates** by configuring the update server
4. **Configure your RustDesk server** at remote.soft1.ch to work with the custom client

## Important Notes

- The builds will be named "SoftConnect" instead of "RustDesk"
- They will connect to your server at `remote.soft1.ch` by default
- The public key `5feZEqWpnFlRUOk03vIG69cyrnkKXrgVsiNCMBAPnng=` is hardcoded
- All branding references have been changed to Soft1/SoftConnect

## Support

For detailed branding information, see `BRANDING.md` in the repository root.

For RustDesk-specific build documentation, refer to the original documentation:
- https://github.com/rustdesk/rustdesk/blob/master/docs/README.md
