import sys
from pathlib import Path

# Add module paths
sys.path.append(str(Path(__file__).parent.parent))

from modules.temporal_segmenter import TemporalSegmenter

def run_modern_pipeline(video_path=None):
    """Chạy modern pipeline"""
    print("🚀 KHỞI CHẠY MODERN PIPELINE")
    print("=" * 50)
    
    # Khởi tạo components
    segmenter = TemporalSegmenter()
    
    # Giả lập video path nếu không có
    if video_path is None:
        video_path = "data/processed/raw_videos_mp4/sample_video.mp4"
        print(f"⚠️  Using sample video path: {video_path}")
    
    # Chạy temporal segmentation
    print("\n1. TEMPORAL SEGMENTATION")
    boundaries = segmenter.detect_boundaries(video_path)
    print(f"   ✅ Detected boundaries: {boundaries}")
    
    # TODO: Thêm các bước tiếp theo
    print("\n2. FEATURE EXTRACTION - [COMING SOON]")
    print("3. SIGN RECOGNITION - [COMING SOON]")
    print("4. GRAMMAR REFINEMENT - [COMING SOON]")
    
    print("\n" + "=" * 50)
    print("🎉 MODERN PIPELINE CHẠY THÀNH CÔNG")

if __name__ == "__main__":
    run_modern_pipeline()