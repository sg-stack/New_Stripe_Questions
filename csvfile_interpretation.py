from datetime import datetime
min_amo=5
max_amo=5000
blocked_methods={"CRYPTO","WIRE"}
error_priority=["ERR_MISSING_FIELD",
    "ERR_AMOUNT_OUT_OF_RANGE",
    "ERR_BLOCKED_PAYMENT_METHOD",
    "ERR_BEHAVIOR_MISMATCH"]
USER_BEHAVIOR = {
    "countries": {"US"},
    "time_range": (9, 18),        # 9 AM to 6 PM
    "amount_range": (50, 500)
}
transactions = [
    {
        "txn_id": "T001",
        "user_id": "U100",
        "amount": "120",
        "currency": "USD",
        "payment_method": "CARD",
        "timestamp": "2025-07-01 10:30",
        "country": "US"
    },
    {
        "txn_id": "T002",
        "user_id": "U100",
        "amount": "100",
        "currency": "USD",
        "payment_method": "CARD",
        "timestamp": "2025-07-01 11:00",
        "country": "US"
    },
    {
        "txn_id": "T003",
        "user_id": "U100",
        "amount": "9500",
        "currency": "USD",
        "payment_method": "CARD",
        "timestamp": "2025-07-01 23:45",
        "country": "US"
    },
    {
        "txn_id": "T004",
        "user_id": "U100",
        "amount": "300",
        "currency": "USD",
        "payment_method": "CRYPTO",
        "timestamp": "2025-07-02 14:20",
        "country": "DE"
    }
]
print(int(transactions[0]["amount"]))
print(f"{'Txnid':<6} Status")
print("-"*40)
def check_integrity_error(i):
    for val in i.values():
        if val.strip()=="":
            return "Integrity_Error"
    return "No Integrity Error"
def high_risk_error(trans):
    print(trans)
    amo=int(trans["amount"])
    meth=trans["payment_method"]
    if amo<min_amo or amo>max_amo or meth in blocked_methods:
        return "Invalid transaction"
    if min_amo<=amo<=max_amo:
        print("no amount restriction")
    if meth in blocked_methods:
        print("Not a blocked transaction")

def match_ratio(trans):
    match=0
    total=3
    if trans["country"] in USER_BEHAVIOR["countries"]:
        match+=1
    txn_hour=datetime.strptime(trans["timestamp"],"%Y-%m-%d %H:%M").hour
    if USER_BEHAVIOR["time_range"][0]<=txn_hour<=USER_BEHAVIOR["time_range"][1]:
        match+=1
    if min_amo<=int(trans["amount"])<=max_amo:
        match+=1
    return match/total
def evaluate_trans(i):
    v=check_integrity_error(i)
    h=[]
    h=high_risk_error(i)
    g=match_ratio(i)
    if g<0.5:
        print("low behavioral match")
  

for i in transactions:
    c=evaluate_trans(i)

    