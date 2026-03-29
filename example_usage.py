"""
使用示例 - 纯 Python 版本
不再需要 Node.js！
"""
import pywencai

# 注意：需要提供有效的 cookie 才能使用
# cookie 获取方法见 README.md

# 示例 1: 基本查询
print("示例 1: 基本查询")
# res = pywencai.get(query='昨日涨幅前10', cookie='your_cookie_here')
# print(res)

# 示例 2: 带排序的查询
print("\n示例 2: 带排序的查询")
# res = pywencai.get(
#     query='退市股票', 
#     sort_key='退市@退市日期', 
#     sort_order='asc',
#     cookie='your_cookie_here'
# )
# print(res)

# 示例 3: 循环分页获取所有数据
print("\n示例 3: 循环分页")
# res = pywencai.get(
#     query='昨日涨幅', 
#     loop=True,  # 获取所有页
#     log=True,   # 显示日志
#     cookie='your_cookie_here'
# )
# print(f"共获取 {len(res)} 条数据")

print("\n✅ 纯 Python 实现，无需 Node.js！")
print("请取消注释并提供有效的 cookie 来运行实际查询。")
