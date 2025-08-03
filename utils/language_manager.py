LANGUAGES = {
    "English": {
        "load_file": "Load File",
        "save_file": "Save File",
        "mean": "Mean",
        "median": "Median",
        "std_dev": "Standard Deviation",
        "correlation": "Correlation",
        "drop_na": "Drop Missing Values",
        "fill_mean": "Fill Missing with Mean",
        "fill_median": "Fill Missing with Median",
        "filter_data": "Filter Data",
        "sort_data": "Sort Data",
        "group_data": "Group Data",
        "plot": "Plot",
        "exit": "Exit"
    },
    "Bangla": {
        "load_file": "ফাইল লোড করুন",
        "save_file": "ফাইল সংরক্ষণ করুন",
        "mean": "গড়",
        "median": "মধ্যক",
        "std_dev": "মানক বিচ্যুতি",
        "correlation": "সহসম্পর্ক",
        "drop_na": "অনুপস্থিত তথ্য মুছুন",
        "fill_mean": "গড় দিয়ে পূরণ করুন",
        "fill_median": "মধ্যক দিয়ে পূরণ করুন",
        "filter_data": "ডাটা ফিল্টার করুন",
        "sort_data": "ডাটা সাজান",
        "group_data": "গ্রুপ ডাটা",
        "plot": "প্লট করুন",
        "exit": "প্রস্থান"
    }
}

def get_text(lang, key):
    return LANGUAGES.get(lang, LANGUAGES["English"]).get(key, key)