from .hexin_v_pure import get_token


def headers(cookie=None, user_agent=None):
    '''生成请求头'''
    if user_agent is None:
        from fake_useragent import UserAgent
        ua = UserAgent()
        user_agent = ua.random
        

    return {
        'hexin-v': get_token(),
        'User-Agent': user_agent,
        'cookie': cookie
    }
