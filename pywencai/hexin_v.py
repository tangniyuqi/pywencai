"""
Python 实现的 hexin-v token 生成器
"""
import time
import random
import hashlib
import base64
from typing import List

class TokenGenerator:
    """Token 生成器"""
    
    def __init__(self):
        self.server_time = int(time.time())
        self.init_state()
    
    def init_state(self):
        """初始化状态"""
        # 初始化各种计数器和状态
        self.mouse_move = 0
        self.mouse_click = 0
        self.mouse_wheel = 0
        self.key_down = 0
        self.click_x = 0
        self.click_y = 0
        self.random_id = self._generate_random_id()
        self.counter = 0
        
    def _generate_random_id(self) -> int:
        """生成随机 ID"""
        return random.randint(0, 0xFFFFFFFF)
    
    def _get_browser_features(self) -> int:
        """获取浏览器特征（模拟）"""
        # 模拟浏览器特征检测结果
        features = [
            True,   # 支持 localStorage
            True,   # 支持 postMessage
            True,   # 支持 Uint8Array
            False,  # 不是 IE
            True,   # 支持 WeakMap
            True,   # Chrome
            False,  # 不是 Safari
            True,   # 支持 canvas
            True,   # 支持 webgl
            False,  # 不是移动端
            True,   # 支持 fetch
            False,  # 不是 PhantomJS
            False,  # 不是自动化工具
            False,  # 其他特征
            False,
            False,
        ]
        
        # 将布尔数组转换为十进制数
        result = 0
        for i, feature in enumerate(features):
            if feature:
                result |= (1 << i)
        return result
    
    def _get_platform(self) -> int:
        """获取平台信息"""
        # 0: Windows, 1: Mac, 2: Linux, 3: Android, 4: iOS
        return 0  # 默认 Windows
    
    def _get_browser_index(self) -> int:
        """获取浏览器索引"""
        # Chrome 的索引
        return 16
    
    def _get_plugin_num(self) -> int:
        """获取插件数量"""
        return 3  # 模拟插件数量
    
    def _str_hash(self, s: str) -> int:
        """字符串哈希"""
        h = 0
        for char in s:
            h = ((h << 5) - h + ord(char)) & 0xFFFFFFFF
        return h
    
    def _encode_buffer(self, data: List[int]) -> str:
        """编码缓冲区数据"""
        # 简单的异或加密
        checksum = self._calculate_checksum(data)
        
        # 添加长度和校验和
        encoded = [len(data) & 0xFF, (checksum >> 24) & 0xFF, (checksum >> 16) & 0xFF, 
                   (checksum >> 8) & 0xFF, checksum & 0xFF]
        
        # 异或加密
        key = checksum
        for byte in data:
            encoded.append((byte ^ (key & 0xFF)) & 0xFF)
            key = (~(key * 0x1505)) & 0xFFFFFFFF
        
        # Base64 编码
        byte_data = bytes(encoded)
        return base64.b64encode(byte_data).decode('ascii')
    
    def _calculate_checksum(self, data: List[int]) -> int:
        """计算校验和"""
        checksum = 0
        for byte in data:
            checksum = ((checksum << 5) - checksum + byte) & 0xFFFFFFFF
        return checksum
    
    def _pack_data(self) -> List[int]:
        """打包数据"""
        # 模拟原始 JS 的数据结构
        # 这里简化了数据结构，只包含关键字段
        data = []
        
        # 添加各种字段（简化版本）
        data.extend(self._int_to_bytes(self.random_id, 4))
        data.extend(self._int_to_bytes(self.server_time, 4))
        data.extend(self._int_to_bytes(int(time.time()), 4))
        data.extend(self._int_to_bytes(self.counter, 2))
        data.extend(self._int_to_bytes(self._get_browser_features(), 2))
        data.extend(self._int_to_bytes(self._get_platform(), 1))
        data.extend(self._int_to_bytes(self._get_browser_index(), 1))
        data.extend(self._int_to_bytes(self._get_plugin_num(), 1))
        
        # 用户代理哈希
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        data.extend(self._int_to_bytes(self._str_hash(user_agent), 4))
        
        # 鼠标和键盘事件
        data.extend(self._int_to_bytes(self.mouse_move, 2))
        data.extend(self._int_to_bytes(self.mouse_click, 2))
        data.extend(self._int_to_bytes(self.mouse_wheel, 2))
        data.extend(self._int_to_bytes(self.key_down, 2))
        data.extend(self._int_to_bytes(self.click_x, 2))
        data.extend(self._int_to_bytes(self.click_y, 2))
        
        return data
    
    def _int_to_bytes(self, value: int, length: int) -> List[int]:
        """将整数转换为字节列表"""
        result = []
        for i in range(length):
            result.append((value >> (i * 8)) & 0xFF)
        return result
    
    def generate(self) -> str:
        """生成 token"""
        # 更新计数器
        self.counter += 1
        
        # 更新时间
        self.server_time = int(time.time())
        
        # 模拟一些用户行为
        self.mouse_move = random.randint(10, 100)
        self.mouse_click = random.randint(1, 10)
        self.mouse_wheel = random.randint(0, 5)
        self.key_down = random.randint(0, 20)
        self.click_x = random.randint(0, 1920)
        self.click_y = random.randint(0, 1080)
        
        # 打包并编码数据
        data = self._pack_data()
        token = self._encode_buffer(data)
        
        return token


# 全局实例
_generator = None


def get_token() -> str:
    """获取 token"""
    global _generator
    if _generator is None:
        _generator = TokenGenerator()
    return _generator.generate()


if __name__ == "__main__":
    # 测试
    print(get_token())
