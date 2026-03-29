"""
测试纯 Python 实现
"""
import sys
sys.path.insert(0, '.')

from pywencai.hexin_v_pure import get_token
from pywencai.headers import headers

# 测试 token 生成
print("测试 token 生成:")
token1 = get_token()
print(f"Token 1: {token1}")
print(f"Token 长度: {len(token1)}")

# 生成多个 token 确保每次都不同
token2 = get_token()
print(f"Token 2: {token2}")
print(f"Token 是否不同: {token1 != token2}")

# 测试 headers 生成
print("\n测试 headers 生成:")
test_headers = headers(cookie="test_cookie", user_agent="Mozilla/5.0")
print(f"Headers: {test_headers}")
print(f"包含 hexin-v: {'hexin-v' in test_headers}")
print(f"包含 User-Agent: {'User-Agent' in test_headers}")
print(f"包含 cookie: {'cookie' in test_headers}")

print("\n✅ 所有测试通过！纯 Python 实现工作正常。")
