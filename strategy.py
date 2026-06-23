from abc import ABC, abstractmethod

class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, files):
        pass
    
class ZipCompressionStrategy(CompressionStrategy):
    def compress(self, files):
        return "zip compress"
    
class RarCompressionStrategy(CompressionStrategy):
    def compress(self, file):
        return "rar compress"
    
class Compressor:
    def __init__(self, strategy: CompressionStrategy):
        self.strategy = strategy
    
    def compress_files(self, files):
        return self.strategy.compress(files)

files = ['f1', 'f2']
zip_compress = Compressor(ZipCompressionStrategy())
rar_compress = Compressor(RarCompressionStrategy())
print(zip_compress.compress_files(files))
print(rar_compress.compress_files(files))