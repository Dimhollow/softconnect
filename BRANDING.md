# SoftConnect Branding Guide

This document outlines the branding changes made to customize RustDesk as **SoftConnect** by **Soft1**.

## Branding Details

- **Company Name**: Soft1
- **Application Name**: SoftConnect
- **Bundle Identifier**: com.soft1.softconnect
- **Copyright**: Copyright © 2025 Soft1. All rights reserved.
- **Email**: info@soft1.ch
- **Server**: remote.soft1.ch
- **Public Key**: 5feZEqWpnFlRUOk03vIG69cyrnkKXrgVsiNCMBAPnng=

## Files Modified

### Core Configuration
- `Cargo.toml` - Main Rust package configuration
  - Package name: softconnect
  - Company: Soft1
  - Bundle identifier: com.soft1.softconnect

### Windows
- `flutter/windows/runner/Runner.rc` - Windows resource file
  - CompanyName: Soft1
  - ProductName: SoftConnect
  - InternalName: softconnect
  - OriginalFilename: softconnect.exe

### macOS
- `flutter/macos/Runner/Configs/AppInfo.xcconfig`
  - PRODUCT_NAME: SoftConnect
  - PRODUCT_BUNDLE_IDENTIFIER: com.soft1.softconnect

### iOS
- `flutter/ios/Runner/Info.plist`
  - CFBundleDisplayName: SoftConnect
  - CFBundleName: SoftConnect
  - URL scheme: softconnect

### Android
- `flutter/android/app/src/main/AndroidManifest.xml`
  - Package: com.soft1.softconnect
  - App label: SoftConnect
- `flutter/android/app/src/main/res/values/strings.xml`
  - app_name: SoftConnect

### Linux
- `res/rustdesk.desktop` - Desktop entry file
  - Name: SoftConnect
  - Exec: softconnect
  - Icon: softconnect
- `res/rustdesk-link.desktop` - Protocol handler
  - Updated to use SoftConnect branding

### Windows Installer
- `res/msi/Package/Language/Package.en-us.wxl`
  - All product references updated to SoftConnect
  - Service name: SoftConnect Service

### Flutter
- `flutter/pubspec.yaml`
  - Description: SoftConnect Remote Desktop

### Server Configuration
- `libs/hbb_common/src/config.rs` - Server and key configuration
  - RENDEZVOUS_SERVERS: remote.soft1.ch
  - RS_PUB_KEY: 5feZEqWpnFlRUOk03vIG69cyrnkKXrgVsiNCMBAPnng=
  - LINK_DOCS_HOME: https://soft1.ch/
  - LINK_DOCS_X11_REQUIRED: https://soft1.ch/

## Logo Files

The following logo files have been created from `flipped.jpeg`:

- `res/icon.png` (512x512) - Main application icon
- `res/mac-icon.png` (512x512) - macOS icon
- `res/32x32.png` - Small icon
- `res/64x64.png` - Medium icon
- `res/128x128.png` - Large icon
- `res/128x128@2x.png` (256x256) - Retina display icon
- `res/mac-tray-dark-x2.png` (22x22) - macOS tray icon (dark mode)
- `res/mac-tray-light-x2.png` (22x22) - macOS tray icon (light mode)
- `flutter/assets/icon.png` - Flutter asset icon

## Additional Steps Required

### 1. Windows ICO File
The Windows `.ico` file needs to be created manually:
- Use an online converter or tool like GIMP to create `res/icon.ico` from `flipped.jpeg`
- Should contain multiple sizes: 16x16, 32x32, 48x48, 256x256
- Update `res/tray-icon.ico` for system tray

### 2. Android Icons
Android requires multiple icon sizes in different density folders. Copy appropriate sized icons to:
- `flutter/android/app/src/main/res/mipmap-hdpi/` (72x72)
- `flutter/android/app/src/main/res/mipmap-mdpi/` (48x48)
- `flutter/android/app/src/main/res/mipmap-xhdpi/` (96x96)
- `flutter/android/app/src/main/res/mipmap-xxhdpi/` (144x144)
- `flutter/android/app/src/main/res/mipmap-xxxhdpi/` (192x192)

Files to replace:
- `ic_launcher.png`
- `ic_launcher_foreground.png`
- `ic_launcher_round.png`
- `ic_stat_logo.png`

### 3. iOS Icons
iOS requires specific icon sizes in `flutter/ios/Runner/Assets.xcassets/AppIcon.appiconset/`:
- Multiple sizes from 20x20 to 1024x1024
- Follow Apple's App Icon specifications

### 4. GitHub Actions Setup

After pushing to GitHub, the automated builds will be triggered. Ensure:
1. GitHub Actions is enabled in your repository
2. The repository has the necessary secrets configured
3. Build workflows are present in `.github/workflows/`

## Building

### Using GitHub Actions (Recommended)
1. Fork this repository to your GitHub account
2. Push changes to your fork
3. GitHub Actions will automatically build for:
   - Windows (x64)
   - macOS (Intel + Apple Silicon)
   - Linux (x64)
   - Android (APK)
   - iOS (requires Apple Developer account)

4. Download the built installers from the GitHub Releases page

### Manual Build
Refer to the original RustDesk documentation for manual build instructions:
- Desktop: `python3 build.py --flutter --release`
- Android: `cd flutter && flutter build android`
- iOS: `cd flutter && flutter build ios`

## Notes

- The branding is comprehensive but you may need to update additional string references in the source code
- Test all builds thoroughly before distributing
- Consider updating the app description, help text, and about dialogs in the source code
- Update any web-based documentation or server configurations to use the new branding
