import cv2
import numpy as np
import os

def calculate_psnr(original_img, processed_img):
    mse = np.mean((original_img - processed_img) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel_value = 255.0
    psnr = 10 * np.log10((max_pixel_value ** 2) / mse)
    return psnr

def calculate_mse(original_img, processed_img):
    mse = np.mean((original_img - processed_img) ** 2)
    return mse

def calculate_mae(original_img, processed_img):
    mae = np.mean(np.abs(original_img - processed_img))
    return mae

# Example folder paths
original_folder_path = r"C:\Users\Hp\Downloads\Train\high"
processed_folder_path = r"./test/predicted/"
results_folder_path = r"./test/results/"

# Create results folder if it doesn't exist
if not os.path.exists(results_folder_path):
    os.makedirs(results_folder_path)

# Get list of files in both folders
original_files = os.listdir(original_folder_path)
processed_files = os.listdir(processed_folder_path)

# Ensure we only process files that are present in both folders
common_files = sorted(set(original_files).intersection(processed_files))

# Open the results file
results_file_path = os.path.join(results_folder_path, "results.txt")
with open(results_file_path, 'w') as results_file:
    # Write the header
    results_file.write(f"{'Image Name':<30} {'PSNR':<15} {'MSE':<15} {'MAE':<15}\n")
    results_file.write("-" * 75 + "\n")
    
    for file_name in common_files:
        # Load images
        original_img_path = os.path.join(original_folder_path, file_name)
        processed_img_path = os.path.join(processed_folder_path, file_name)
        
        original_img = cv2.imread(original_img_path)
        processed_img = cv2.imread(processed_img_path)
        
        # Convert to grayscale if needed
        if len(original_img.shape) > 2:
            original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
        if len(processed_img.shape) > 2:
            processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
        
        # Calculate metrics
        psnr_score = calculate_psnr(original_img, processed_img)
        mse_score = calculate_mse(original_img, processed_img)
        mae_score = calculate_mae(original_img, processed_img)
        
        # Write results to the file
        results_file.write(f"{file_name:<30} {psnr_score:<15.4f} {mse_score:<15.4f} {mae_score:<15.4f}\n")

print("Done!")