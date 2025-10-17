#!/usr/bin/env python3
"""
MAIN EXECUTION SCRIPT - SIGN LANGUAGE RECOGNITION PIPELINE
Chạy: python run_pipeline.py --mode [benchmark|modern|hybrid]
"""

import argparse
import sys
from pathlib import Path

# Add current directory to path để import config
sys.path.append(str(Path(__file__).parent))

from configs.paths import DATA_PATHS, MODEL_PATHS

def run_benchmark_mode():
    """Chạy benchmark trên legacy models"""
    print("🚀 Chạy legacy benchmark...")
    # Implementation sẽ thêm sau
    
def run_modern_mode():
    """Chạy modern pipeline"""
    print("🚀 Chạy modern pipeline...") 
    # Implementation sẽ thêm sau

def run_hybrid_mode():
    """Chạy hybrid approach"""
    print("🚀 Chạy hybrid pipeline...")
    # Implementation sẽ thêm sau

def main():
    parser = argparse.ArgumentParser(description='Sign Language Recognition Pipeline')
    parser.add_argument('--mode', choices=['benchmark', 'modern', 'hybrid'], 
                       default='benchmark', help='Chế độ chạy')
    
    args = parser.parse_args()
    
    print(f"🎯 Bắt đầu pipeline với mode: {args.mode}")
    print(f"📁 Data path: {DATA_PATHS['raw_videos']}")
    
    if args.mode == 'benchmark':
        run_benchmark_mode()
    elif args.mode == 'modern':
        run_modern_mode() 
    elif args.mode == 'hybrid':
        run_hybrid_mode()

if __name__ == "__main__":
    main()
