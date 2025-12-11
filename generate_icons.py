#!/usr/bin/env python3
"""
Icon Generator for SoftConnect
Generates Windows ICO files and Android/iOS icon sets from the source logo
"""

import os
import subprocess
import sys

def run_command(cmd, description):
    """Run a shell command and print status"""
    print(f"→ {description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ⚠️  Warning: {result.stderr.strip()}")
        return False
    print(f"  ✓ Done")
    return True

def create_android_icons():
    """Create Android icon sets"""
    print("\n📱 Creating Android icons...")

    logo_src = "res/softconnect-logo.jpg"
    android_base = "flutter/android/app/src/main/res"

    icon_configs = [
        ("mipmap-mdpi", 48),
        ("mipmap-hdpi", 72),
        ("mipmap-xhdpi", 96),
        ("mipmap-xxhdpi", 144),
        ("mipmap-xxxhdpi", 192),
    ]

    for folder, size in icon_configs:
        path = f"{android_base}/{folder}"
        os.makedirs(path, exist_ok=True)

        # Create launcher icon
        run_command(
            f"sips -s format png -z {size} {size} {logo_src} --out {path}/ic_launcher.png",
            f"Creating {folder}/ic_launcher.png ({size}x{size})"
        )

        # Copy for foreground and round icons
        run_command(
            f"cp {path}/ic_launcher.png {path}/ic_launcher_foreground.png",
            f"Creating {folder}/ic_launcher_foreground.png"
        )
        run_command(
            f"cp {path}/ic_launcher.png {path}/ic_launcher_round.png",
            f"Creating {folder}/ic_launcher_round.png"
        )

        # Create smaller notification icon
        notif_size = max(24, size // 4)
        run_command(
            f"sips -s format png -z {notif_size} {notif_size} {logo_src} --out {path}/ic_stat_logo.png",
            f"Creating {folder}/ic_stat_logo.png ({notif_size}x{notif_size})"
        )

def create_ios_icons():
    """Create iOS icon sets"""
    print("\n🍎 Creating iOS icons...")

    logo_src = "res/softconnect-logo.jpg"
    ios_base = "flutter/ios/Runner/Assets.xcassets/AppIcon.appiconset"

    os.makedirs(ios_base, exist_ok=True)

    # iOS icon sizes (size, scale, filename)
    ios_configs = [
        (20, 2, "Icon-App-20x20@2x.png", 40),
        (20, 3, "Icon-App-20x20@3x.png", 60),
        (29, 2, "Icon-App-29x29@2x.png", 58),
        (29, 3, "Icon-App-29x29@3x.png", 87),
        (40, 2, "Icon-App-40x40@2x.png", 80),
        (40, 3, "Icon-App-40x40@3x.png", 120),
        (60, 2, "Icon-App-60x60@2x.png", 120),
        (60, 3, "Icon-App-60x60@3x.png", 180),
        (76, 2, "Icon-App-76x76@2x.png", 152),
        (83.5, 2, "Icon-App-83.5x83.5@2x.png", 167),
        (1024, 1, "Icon-App-1024x1024@1x.png", 1024),
    ]

    for size, scale, filename, actual_size in ios_configs:
        run_command(
            f"sips -s format png -z {actual_size} {actual_size} {logo_src} --out {ios_base}/{filename}",
            f"Creating {filename} ({actual_size}x{actual_size})"
        )

    # Create Contents.json
    contents_json = """{
  "images" : [
    {
      "size" : "20x20",
      "idiom" : "iphone",
      "filename" : "Icon-App-20x20@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "20x20",
      "idiom" : "iphone",
      "filename" : "Icon-App-20x20@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "Icon-App-29x29@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "Icon-App-29x29@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "40x40",
      "idiom" : "iphone",
      "filename" : "Icon-App-40x40@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "40x40",
      "idiom" : "iphone",
      "filename" : "Icon-App-40x40@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "60x60",
      "idiom" : "iphone",
      "filename" : "Icon-App-60x60@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "60x60",
      "idiom" : "iphone",
      "filename" : "Icon-App-60x60@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "76x76",
      "idiom" : "ipad",
      "filename" : "Icon-App-76x76@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "83.5x83.5",
      "idiom" : "ipad",
      "filename" : "Icon-App-83.5x83.5@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "1024x1024",
      "idiom" : "ios-marketing",
      "filename" : "Icon-App-1024x1024@1x.png",
      "scale" : "1x"
    }
  ],
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}"""

    with open(f"{ios_base}/Contents.json", "w") as f:
        f.write(contents_json)
    print("  ✓ Created Contents.json")

def create_windows_icons_note():
    """Print note about Windows ICO files"""
    print("\n🪟 Windows ICO files:")
    print("  ⚠️  Windows ICO files need special tools to create.")
    print("  📝 Options:")
    print("     1. Use an online converter: https://convertio.co/png-ico/")
    print("     2. Use GIMP (free): Export as .ico with multiple sizes")
    print("     3. Use ImageMagick: brew install imagemagick")
    print("")
    print("  📋 Files needed:")
    print("     - res/icon.ico (16, 32, 48, 256 sizes)")
    print("     - res/tray-icon.ico (16, 32 sizes)")
    print("     - flutter/windows/runner/resources/app_icon.ico")

def main():
    print("🎨 SoftConnect Icon Generator\n")
    print("=" * 60)

    # Check if logo exists
    if not os.path.exists("res/softconnect-logo.jpg"):
        print("❌ Error: res/softconnect-logo.jpg not found!")
        print("   Make sure you're running this from the repository root.")
        sys.exit(1)

    create_android_icons()
    create_ios_icons()
    create_windows_icons_note()

    print("\n" + "=" * 60)
    print("✅ Icon generation complete!")
    print("\n📦 Next steps:")
    print("   1. Create Windows ICO files (see options above)")
    print("   2. Commit the new icons: git add . && git commit -m 'Add icon sets'")
    print("   3. Push to GitHub to trigger automated builds")

if __name__ == "__main__":
    main()
