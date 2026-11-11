#include <cuda_runtime.h>
#include <vector>
// CUDA kernel: chạy song song trên GPU
__global__ void index_kernel(int* out, int n) {
    // Compute this thread's global index and, if it is < n, write it to out.
    // Tính chỉ số toàn cục global index của thread
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    // Boundary guard: Đảm bảo không truy cập ngoài phạm vi mảng
    if (i < n) {
        out[i] = i;
    }
}
// Host Wrapper: Hàm trên CPU quản lý cấp phát, thực thi và truyền nhận bộ nhớ
std::vector<int> global_thread_indices(int n) {
    // 1. allocate device memory for n ints
    if (n <= 0) {
        return std::vector<int>();
    }
    // 2. launch the kernel with enough threads to cover n
    std::vector<int> result(n);
    int* d_out = nullptr;
    size_t size = n * sizeof(int);
    // Bước 1: cấp phát vram trên device (gpu)
    cudaMalloc((void**)&d_out, size);
    // Bước 2: Cấu hình số lượng Thread và Block
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock; // làm tròn lên
    // Bước 3: Launch Kernel thực thi trên GPU
    index_kernel<<<blocksPerGrid, threadsPerBlock>>>(d_out, n);
    // 3. copy the result back to the host and return it
    // Bước 4: Sao chép dữ liệu từ Vram về ram
    cudaMemcpy(result.data(), d_out, size, cudaMemcpyDeviceToHost);
    // Bước 5: giải phóng vram cho gpu
    cudaFree(d_out);
    return result;
}
