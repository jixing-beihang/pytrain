from datetime import datetime, timezone, timedelta

# 获取当前时间
now = datetime.now()
print(now)
# datetime 转换为timestamp
print(now.timestamp())
# timestamp 转换为 datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))

# datetime 转换为 str
print(datetime.strftime(datetime.now(),'%Y%m%d%H%M%S'))
# str 转换为 datetime
print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))

# 设置时区
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('伦敦时间：',utc_dt,'北京时间：',bj_dt)