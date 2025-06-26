# password_strength.py
from zxcvbn import password_strength

def analyze_password_strength(password):
    result = password_strength(password)
    score = result['score']
    feedback = result['feedback']

    return {
        'score': score,
        'crack_time': result['crack_times_display']['offline_slow_hashing_1e4_per_second'],
        'feedback': feedback
    }
