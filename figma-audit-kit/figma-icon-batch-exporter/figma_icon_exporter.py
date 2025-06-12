#!/usr/bin/env python3
"""
Figma Icon Library Batch Exporter

A Python script for batch exporting SVG icons from Figma component libraries 
with support for component variants, page filtering, and intelligent naming conventions.

Author: Steven Villarino
License: MIT
"""

import os
import requests
from pathlib import Path

# Try to import configuration from config.py, fallback to environment variables or defaults
try:
    from config import *
except ImportError:
    print("config.py not found. Using environment variables or edit this script directly.")
    
    # --- Configuration ---
    # Get from environment variables or set directly here
    FIGMA_FILE_KEY = os.getenv('FIGMA_FILE_KEY', 'your-figma-file-key-here')
    FIGMA_TOKEN = os.getenv('FIGMA_TOKEN', 'your-figma-token-here')
    
    # Optional: Specify which page to export from (leave empty to export from all pages)
    TARGET_PAGE_NAME = os.getenv('TARGET_PAGE_NAME', None)  # Set to None or "" to export from all pages
    
    # Add the specific component names you want to export
    COMPONENT_NAMES = [
        "!20Hz",
        "1080p",
        "120Hz",
        "1440p",
        "2K",
        "4K",
        "4KHDR",
        "4KPictureHDR",
        "4KUltraHD",
        "8K",
        "8KHDR",
        "AVSync",
        "AlignVerticalCenter",
        "AlignVerticalTop",
        "ArrowLineDown",
        "AudioMute",
        "BacklitButton",
        "BatteryCharging",
        "BatteryChargingDynamic",
        "BatteryEmpty",
        "Bookmark",
        "Camera",
        "Camera360",
        "Camera360Pan",
        "Camera360PanTilt",
        "Circle",
        "CircleFilled",
        "ClosedCaptions",
        "Cloud",
        "CloudOffline",
        "CloudStorage",
        "CollapseFullscreen",
        "DevicesAll",
        "Download",
        "DownloadFilled",
        "Error",
        "ErrorCircle",
        "ErrorCircleFilled",
        "ErrorTriangle",
        "ErrorTriangleFilled",
        "ExpandFullScreen",
        "ExpertPictureMode",
        "FHD1080P",
        "FHD1080p",
        "Fastforward",
        "FastforwardCircle",
        "Flo",
        "FolderFilled",
        "GiftBox",
        "GroupAdd",
        "GuideWordmark",
        "HD720",
        "HDR",
        "HDR10+",
        "HeadToToeView",
        "Headphones",
        "ImageReset",
        "Info",
        "InfoCircle",
        "InfoCircleFilled",
        "LED",
        "Location",
        "Logout",
        "LogoutFilled",
        "MicrophoneMute",
        "MiniLED",
        "Moon",
        "MoonAuto",
        "MoonOff",
        "MoonOn",
        "MoonStars",
        "MotionTracking",
        "MovieSlate",
        "MovieSlateWink",
        "Notes",
        "OLED",
        "Odometer",
        "PackageNotification",
        "PageViews",
        "PetDetection",
        "PhotoAlbum",
        "PlayCircle",
        "Power",
        "ProfileAdd",
        "ProfileAddFilled",
        "QLED",
        "QuestionMark",
        "QuestionMarkCircle",
        "Record",
        "Refresh",
        "Replay",
        "Route",
        "Save",
        "ShieldLock",
        "SingleView",
        "Square",
        "StreamingStick",
        "StreamingStickRoku",
        "Sun",
        "TV4K",
        "TV4KHDR",
        "TV8K",
        "TVAudio",
        "TVCheckmark",
        "TVFHD",
        "TVFree",
        "TVHD",
        "TVLandscape",
        "TVLightning",
        "TVLiveTV",
        "TVPlay",
        "TVRokuChannel",
        "TVRokuTVReady",
        "TVScreenSize",
        "TVSparkle",
        "TVStar",
        "TVWink",
        "Table",
        "Tag",
        "TicketCheckmark",
        "TicketFree",
        "TicketLightning",
        "TicketLive",
        "TicketPlay",
        "TicketSparkle",
        "TicketStar",
        "TicketWink",
        "Timejump",
        "Timelapse",
        "Trivia",
        "ULED4K",
        "USB",
        "USB-C",
        "Upload",
        "ViewFisheye",
        "ViewSquare",
        "WiFiHub",
        "WifiRange"
    ]
    
    # Output settings
    OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'exported_icons')
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', '100'))

# Validate required configuration
if FIGMA_FILE_KEY == 'your-figma-file-key-here' or not FIGMA_FILE_KEY:
    print("❌ Error: Please set your FIGMA_FILE_KEY")
    print("   Either edit this script or create a config.py file")
    exit(1)

if FIGMA_TOKEN == 'your-figma-token-here' or not FIGMA_TOKEN:
    print("❌ Error: Please set your FIGMA_TOKEN")
    print("   Either edit this script or create a config.py file")
    exit(1)

HEADERS = {
    'X-Figma-Token': FIGMA_TOKEN
}

def main():
    """Main function to export Figma icons"""
    print("🚀 Figma Icon Library Batch Exporter")
    print("=" * 50)
    
    # --- Step 1: Get file components ---
    print("📡 Fetching components...")
    try:
        print(f"Making request to: https://api.figma.com/v1/files/{FIGMA_FILE_KEY}/components")
        print(f"Using token: {FIGMA_TOKEN[:10]}...")
        
        res = requests.get(
            f'https://api.figma.com/v1/files/{FIGMA_FILE_KEY}/components', 
            headers=HEADERS
        )
        
        print(f"Response status code: {res.status_code}")
        
        if res.status_code != 200:
            print(f"❌ HTTP Error {res.status_code}: {res.text}")
            exit(1)
        
        response_data = res.json()
        print(f"API response keys: {list(response_data.keys())}")
        
        # Check for actual API errors (not the 'status' field)
        if 'error' in response_data and response_data['error']:
            print(f"❌ Error from Figma API: {response_data['error']}")
            exit(1)
        
        # The components are directly in the 'meta' -> 'components' path
        components = response_data.get('meta', {}).get('components', [])
        if not components:
            print("❌ No components found in the file")
            exit(1)
            
        print(f"✅ Found {len(components)} components in total")
        
        # --- Step 2: Filter by specific names and optionally by page ---
        if COMPONENT_NAMES:
            # Extract the actual component names from the containing_frame
            filtered = []
            for c in components:
                component_name = c.get('containing_frame', {}).get('name', '')
                page_name = c.get('containing_frame', {}).get('pageName', '')
                
                # Check if component name matches
                name_matches = component_name in COMPONENT_NAMES
                
                # Check if page matches (if TARGET_PAGE_NAME is specified)
                page_matches = True  # Default to True if no page filter
                if TARGET_PAGE_NAME:
                    page_matches = page_name == TARGET_PAGE_NAME
                
                if name_matches and page_matches:
                    filtered.append(c)
            
            print(f"✅ Found {len(filtered)} matching components from your list")
            if TARGET_PAGE_NAME:
                print(f"📄 Filtered to page: '{TARGET_PAGE_NAME}'")
            
            # Debug: Show which components were found and which were missing
            found_names = [c.get('containing_frame', {}).get('name', '') for c in filtered]
            missing_names = [name for name in COMPONENT_NAMES if name not in found_names]
            
            # Also show which pages the found components are from
            found_pages = list(set([c.get('containing_frame', {}).get('pageName', 'Unknown') for c in filtered]))
            print(f"📄 Found components on pages: {', '.join(found_pages)}")
            
            if found_names:
                print(f"🎯 Found components: {', '.join(found_names[:10])}{'...' if len(found_names) > 10 else ''}")
            if missing_names:
                print(f"❓ Missing components: {', '.join(missing_names[:10])}{'...' if len(missing_names) > 10 else ''}")
        else:
            print("❌ Please specify component names in the COMPONENT_NAMES list")
            exit(1)
        
        # --- Step 3: Request SVG export URLs ---
        if not filtered:
            print("❌ No matching components found to export")
            print("📋 Available component names in the file:")
            all_names = [c.get('containing_frame', {}).get('name', 'Unknown') for c in components]
            unique_names = sorted(set(all_names))
            
            # Also show available pages
            all_pages = [c.get('containing_frame', {}).get('pageName', 'Unknown') for c in components]
            unique_pages = sorted(set(all_pages))
            print(f"📄 Available pages: {', '.join(unique_pages)}")
            
            for name in unique_names[:20]:  # Show first 20
                print(f"  - {name}")
            if len(unique_names) > 20:
                print(f"  ... and {len(unique_names) - 20} more")
            exit(1)
            
        ids = [c['node_id'] for c in filtered]
        if not ids:
            print("❌ No valid node IDs found")
            exit(1)
        
        # Figma API has limits, so let's batch the requests if we have too many components
        batch_size = BATCH_SIZE  # Process in smaller batches
        all_images = {}
        
        for i in range(0, len(ids), batch_size):
            batch_ids = ids[i:i+batch_size]
            ids_query = ",".join(batch_ids)
            print(f"📥 Requesting SVG export URLs for batch {i//batch_size + 1} ({len(batch_ids)} components)...")
            
            images_res = requests.get(
                f'https://api.figma.com/v1/images/{FIGMA_FILE_KEY}?ids={ids_query}&format=svg',
                headers=HEADERS
            )
            
            if images_res.status_code != 200:
                print(f"❌ Error requesting images for batch {i//batch_size + 1}: {images_res.status_code}")
                print(f"Response: {images_res.text}")
                continue
                
            images_data = images_res.json()
            print(f"✅ Batch {i//batch_size + 1} - Images API response keys: {list(images_data.keys())}")
            
            # Check for actual errors in the images response
            if 'err' in images_data and images_data['err'] is not None:
                print(f"❌ Figma API error for batch {i//batch_size + 1}: {images_data['err']}")
                continue
            
            # Check if we have the images data
            if 'images' not in images_data:
                print(f"❌ No 'images' key in response for batch {i//batch_size + 1}. Keys available: {list(images_data.keys())}")
                continue
                
            batch_images = images_data.get('images', {})
            all_images.update(batch_images)
            print(f"✅ Batch {i//batch_size + 1} successfully processed: {len(batch_images)} URLs received")
        
        images = all_images
        
        # --- Step 4: Download SVGs ---
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        print(f"📁 Created output directory: {OUTPUT_DIR}")
        
        print(f"⬇️  Downloading {len(images)} SVGs...")
        successful_downloads = 0
        
        for comp in filtered:
            node_id = comp['node_id']
            # Use the containing frame name as the parent component name
            parent_name = comp.get('containing_frame', {}).get('name', 'unknown')
            # Extract variant from the name field (e.g., "Variant=Solid" -> "Solid")
            variant_name = comp.get('name', 'unknown')
            if variant_name.startswith('Variant='):
                variant_name = variant_name.replace('Variant=', '')
            
            # Combine parent and variant: "ClosedCaptions-Solid"
            name = f"{parent_name}-{variant_name}"
            name = name.replace(" ", "").replace("/", "_").replace("!", "").replace("+", "Plus")  # Sanitize filename
            url = images.get(node_id)
            
            if url:
                try:
                    svg_response = requests.get(url)
                    svg_response.raise_for_status()
                    svg_data = svg_response.content
                    
                    file_path = f"{OUTPUT_DIR}/{name}.svg"
                    with open(file_path, 'wb') as f:
                        f.write(svg_data)
                    print(f"✅ Exported {name}.svg")
                    successful_downloads += 1
                except Exception as e:
                    print(f"❌ Failed to export {name}.svg: {str(e)}")
            else:
                print(f"❌ No URL available for {name}")
        
        print("=" * 50)
        print(f"🎉 Export complete!")
        print(f"✅ Successfully downloaded {successful_downloads} out of {len(filtered)} icons.")
        print(f"📁 Icons saved to: {os.path.abspath(OUTPUT_DIR)}")
        
        if successful_downloads < len(filtered):
            failed_count = len(filtered) - successful_downloads
            print(f"⚠️  {failed_count} icons failed to download. Check the output above for details.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error making request to Figma API: {str(e)}")
        exit(1)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    main()
