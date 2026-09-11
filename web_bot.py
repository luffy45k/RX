import urllib.request
import json
import random
import os

MEMORY_FILE = "game_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(new_entry):
    memory = load_memory()
    memory.append(new_entry)
    try:
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=4)
    except:
        pass

def upgraded_quantum_math(open_p, close_p):
    try:
        o_digits = [int(ch) for ch in str(open_p) if ch.isdigit()]
        c_digits = [int(ch) for ch in str(close_p) if ch.isdigit()]
        if len(o_digits) < 3: o_digits = [1, 9, 0]
        if len(c_digits) < 3: c_digits = [2, 4, 9]

        sum_o = sum(o_digits)
        sum_c = sum(c_digits)
        single_o = sum_o % 10
        single_c = sum_c % 10
        derived_jodi = f"{single_o}{single_c}"
        
        fib = [1, 2, 3, 5, 8]
        weighted_o = sum(d * fib[i % len(fib)] for i, d in enumerate(o_digits))
        weighted_c = sum(d * fib[(i+1) % len(fib)] for i, d in enumerate(c_digits))
        quantum_index = (weighted_o + weighted_c + (single_o * 7) + (single_c * 3)) % 100
        return single_o, single_c, derived_jodi, quantum_index
    except:
        return 0, 0, "00", 0

print("🚀 Next-Gen Prediction Bot Active! (Exit ke liye 'quit' likhein)")
markets = ["KALYAN", "MADHUR MORNING", "SRIDEVI", "TIME BAZAR", "MILAN DAY"]

while True:
    print("\n-------------------------------------------------------------------")
    print("CHOOSE AN OPTION:")
    print("1. Random Generate karein")
    print("2. Custom Record daalein (jaise 190-05-249)")
    print("3. Next Number Smart Prediction (Historical Trend Analysis)")
    
    choice = input("Apna option chunein (1, 2, 3 ya Enter dabayein): ").strip()
    if choice.lower() in ['quit', 'exit']:
        print("Alvida! 👋")
        break

    open_panna = ""
    close_panna = ""
    jodi_num = ""
    selected_market = random.choice(markets)

    if choice == "1":
        open_panna = f"{random.randint(1,9)}{random.randint(0,9)}{random.randint(0,9)}"
        close_panna = f"{random.randint(1,9)}{random.randint(0,9)}{random.randint(0,9)}"
    elif choice == "2":
        custom_input = input("Custom Record daalein (jaise 190-05-249): ").strip()
        parts = [p.strip() for p in custom_input.split('-') if p.strip()]
        if len(parts) >= 3:
            open_panna = parts[0]
            jodi_num = parts[1]
            close_panna = parts[2]
        else:
            open_panna = f"{random.randint(1,9)}{random.randint(0,9)}{random.randint(0,9)}"
            close_panna = f"{random.randint(1,9)}{random.randint(0,9)}{random.randint(0,9)}"
    else:
        # Option 3: Smart Next Number Prediction based on history
        memory_db = load_memory()
        print("[System]: Historical memory se next number pattern analyze ho raha hai...")
        if len(memory_db) >= 2:
            last_rec = memory_db[-1].get("record", "190-05-249")
            parts = last_rec.split('-')
            if len(parts) == 3:
                prev_open, prev_jodi, prev_close = parts[0], parts[1], parts[2]
                # Shift digits for next prediction trend
                open_panna = f"{(int(prev_close[0])+1)%10}{random.randint(0,9)}{random.randint(0,9)}"
                close_panna = f"{random.randint(1,9)}{random.randint(0,9)}{(int(prev_open[2])+2)%10}"
            else:
                open_panna = f"{random.randint(1,9)}{random.randint(0,9)}{random.randint(0,9)}"
                close_panna = f"{random.randint(1,9)}{random.randint(0,9)}{random.randint(0,9)}"
        else:
            open_panna = "579"
            close_panna = "567"

    o_dig, c_dig, calc_jodi, quantum_index = upgraded_quantum_math(open_panna, close_panna)
    if not jodi_num:
        jodi_num = calc_jodi

    save_memory({"market": selected_market, "record": f"{open_panna}-{jodi_num}-{close_panna}", "quantum_index": quantum_index})
    total_records = len(load_memory())

    print(f"\n📊 --- {selected_market} NEXT PREDICTION RESULT ---")
    print(f"📦 Box Format: [{open_panna}]  -  [{jodi_num}]  -  [{close_panna}]")
    print(f"🧮 Quantum Trend -> Open Digit: {o_dig} | Close Digit: {c_dig} | Momentum Index: {quantum_index:02d}")
    print(f"💾 Saved to DB! Total Records: {total_records}")
