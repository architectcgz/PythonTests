def find_effort():
    # 样本数据
    rest_day_decrease = 0.01
    total_days = 365
    work_days = total_days * 5 / 7
    rest_days = total_days - work_days
    target = 37.78

    # 使用二分查找法找到合适的努力程度
    low, high = 0, 1
    while high - low > 1e-6:
        mid = (low + high) / 2
        if (1 - rest_day_decrease) ** rest_days * (1 + mid) ** work_days < target:
            low = mid
        else:
            high = mid

    return low


# 测试函数
print(f'工作日要努力{find_effort() * 100:.3f}%')
