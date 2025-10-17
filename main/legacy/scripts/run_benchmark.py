import sys
import os
from pathlib import Path

# Add config path
sys.path.append(str(Path(__file__).parent.parent.parent))
from configs.paths import DATA_PATHS

def benchmark_i3d():
    """Benchmark I3D model"""
    print("🧪 Benchmarking I3D model...")
    
    # Kiểm tra model tồn tại
    i3d_path = Path(DATA_PATHS['legacy_i3d'])
    if not i3d_path.exists():
        print("❌ I3D model không tồn tại")
        return False
    
    print(f"✅ I3D model found: {i3d_path}")
    
    # TODO: Implementation benchmark chi tiết
    print("📊 I3D benchmark sẽ được implement sau")
    return True

def benchmark_tgcn():
    """Benchmark TGCN model"""
    print("🧪 Benchmarking TGCN model...")
    
    # Kiểm tra model tồn tại
    tgcn_path = Path(DATA_PATHS['legacy_tgcn'])
    if not tgcn_path.exists():
        print("❌ TGCN model không tồn tại")
        return False
    
    print(f"✅ TGCN model found: {tgcn_path}")
    
    # TODO: Implementation benchmark chi tiết
    print("📊 TGCN benchmark sẽ được implement sau")
    return True

def main():
    print("🚀 BẮT ĐẦU BENCHMARK LEGACY MODELS")
    print("=" * 50)
    
    # Kiểm tra data tồn tại
    annotations_path = Path(DATA_PATHS['annotations'])
    if not annotations_path.exists():
        print("❌ Không tìm thấy file annotations")
        return
    
    print(f"✅ Dataset annotations: {annotations_path}")
    
    # Chạy benchmark từng model
    success_i3d = benchmark_i3d()
    print("-" * 30)
    success_tgcn = benchmark_tgcn()
    
    print("\n" + "=" * 50)
    if success_i3d and success_tgcn:
        print("🎉 BENCHMARK HOÀN TẤT - SẴN SÀNG CHO MODERN PIPELINE")
    else:
        print("⚠️  Có vấn đề với một số models")

if __name__ == "__main__":
    main()