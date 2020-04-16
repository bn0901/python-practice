# ==========基础部门代码================================
def get_company_money():
    """公司收入120万"""
    return 120


def get_lizhi():
    """离职率0.3"""
    return 0.3


def wrapper(func):
    def inner():
        print("权限验证代码")
        func()
    return inner

# ================高级部门代码==================================
get_company_money = wrapper(get_company_money)
get_company_money()

get_lizhi = wrapper(get_lizhi)
get_lizhi()


# =========================装饰器=======================================

# ==========基础部门代码================================
@wrapper
def get_company_money():
    """公司收入120万"""
    return 120

@wrapper
def get_lizhi():
    """离职率0.3"""
    return 0.3


def wrapper(func):
    def inner():
        print("权限验证代码")
        func()
    return inner

# ================高级部门代码==================================
money = get_company_money()
lizi = get_lizhi()
print(F'公司收入:{money},公司离职率:{lizi}')