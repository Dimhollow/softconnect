# SoftConnect - Quick Start Guide

## ✅ What's Been Done

Your RustDesk client has been fully rebranded as **SoftConnect** by **Soft1**:

- ✅ All configuration files updated
- ✅ Server configured: `remote.soft1.ch`
- ✅ Public key configured: `5feZEqWpnFlRUOk03vIG69cyrnkKXrgVsiNCMBAPnng=`
- ✅ Email updated to: `info@soft1.ch`
- ✅ All platform icons created (Windows, macOS, Linux, Android, iOS)
- ✅ All changes committed to Git

## 📤 Next Step: Push to GitHub

### Option 1: Use the Setup Script (Easiest)

```bash
cd /Users/davuddemic/Repositories/rustdesk
./setup_github.sh
```

The script will:
1. Ask for your GitHub username
2. Guide you to create the repository on GitHub
3. Push all the code automatically

### Option 2: Manual Setup

1. **Create GitHub Repository**
   - Go to https://github.com/new
   - Repository name: `softconnect` (or your choice)
   - Choose Private or Public
   - **DO NOT** initialize with README
   - Click "Create repository"

2. **Push the Code**
   ```bash
   cd /Users/davuddemic/Repositories/rustdesk
   git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
   git push -u origin master
   ```

## 📥 Downloading Your Builds

### After GitHub Actions Complete (~30-60 minutes):

1. Go to your repository: `https://github.com/YOUR_USERNAME/REPO_NAME`
2. Click the "Actions" tab to watch the build progress
3. Once complete, go to the "Releases" section
4. Download the installers:

   **Windows:**
   - `SoftConnect-x86_64.exe` - 64-bit installer
   - `SoftConnect-x86_64.msi` - MSI package

   **macOS:**
   - `SoftConnect.dmg` - Universal installer (Intel + M1/M2)

   **Linux:**
   - `SoftConnect-x86_64.AppImage` - Universal Linux app
   - `SoftConnect-x86_64.deb` - Debian/Ubuntu package
   - `SoftConnect-x86_64.rpm` - RedHat/Fedora package

   **Android:**
   - `SoftConnect.apk` - Android app

   **iOS:**
   - Requires Apple Developer account and manual signing

## 🔑 Important Information

Your clients will automatically connect to:
- **Server**: `remote.soft1.ch`
- **Port**: 21116 (default RustDesk port)
- **Public Key**: Pre-configured

Make sure your RustDesk server is running at `remote.soft1.ch:21116`!

## 🛠️ Testing Before GitHub

If you want to test locally before pushing:

### Test macOS Build (on your Mac):
```bash
cd /Users/davuddemic/Repositories/rustdesk
python3 build.py --flutter --release
```

The built app will be in: `target/release/`

### Test Android Build:
```bash
cd /Users/davuddemic/Repositories/rustdesk/flutter
flutter build apk --release
```

The APK will be in: `build/app/outputs/flutter-apk/`

## 📞 Support Files

- `BRANDING.md` - Complete list of all branding changes
- `GITHUB_SETUP.md` - Detailed GitHub setup instructions
- `generate_icons.py` - Icon generator script (already run)
- `setup_github.sh` - Automated GitHub setup script

## 🎯 What Happens on GitHub

When you push to GitHub, GitHub Actions will automatically:

1. **Build for all platforms in parallel**
2. **Create installers and packages**
3. **Upload to GitHub Releases**

You just need to wait for the builds to complete and download them!

## ⚠️ Common Issues

**Build fails?**
- Check GitHub Actions logs for specific errors
- Ensure your server at `remote.soft1.ch` is accessible

**Icons not showing?**
- All icons have been generated - they should work!
- Windows ICO files: ✅ Created
- Android icons: ✅ Created (all densities)
- iOS icons: ✅ Created (all sizes)

**Can't push to GitHub?**
- Make sure you have Git configured:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

## 🚀 Ready to Go!

Everything is ready. Just run:

```bash
cd /Users/davuddemic/Repositories/rustdesk
./setup_github.sh
```

And follow the prompts!
