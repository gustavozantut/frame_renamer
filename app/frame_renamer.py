import os
import time
from pathlib import Path
from shutil import copyfile

detect_dir = Path("/detect")
old_det_dir = detect_dir / "old"

def get_latest_detection_name(detect_dir=detect_dir,old_det_dir=old_det_dir):
    
    latest_detection_name = sorted(
        [item
         for item in detect_dir.glob("*")
         if not os.path.samefile(item, old_det_dir)
         and not os.path.commonpath([item, old_det_dir]) == old_det_dir
         ],
        key=lambda x: x.stat().st_mtime,
        reverse=True,
    )[0].name
    
    return latest_detection_name

def main():

    while not [
        item
        for item in detect_dir.glob("*")
        if not os.path.samefile(item, old_det_dir)
        and not os.path.commonpath([item, old_det_dir]) == old_det_dir
    ]:
        
        time.sleep(0.5)

    latest_detection = get_latest_detection_name(detect_dir)
    frames_dir = detect_dir / latest_detection / "frames"
    stream_frames_dir = frames_dir / "frames_stream"
    os.makedirs(stream_frames_dir, exist_ok=True)

    while not os.path.exists(stream_frames_dir):
        
        time.sleep(0.5)
        
    renamed_files=[]
    
    while True:
        
        try:
        
            for filename in sorted([os.path.join(frames_dir, file) for file in os.listdir(frames_dir) if os.path.isfile(os.path.join(frames_dir, file))]):
                
                if filename in renamed_files:
                    print("no more frames to rename.")
                    return 1

                copyfile(frames_dir / filename, stream_frames_dir / f"frame_{renamed_frames}.png")
                renamed_files.append(filename)
                
                
              
                    

            time.sleep(0.5)
        
        except:
            
            print("no more frames to rename.")
            return 1
                                    
if __name__ == "__main__":
    
    time.sleep(5)
    main()
