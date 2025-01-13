import time

def play_sos_and_display_contacts():
    # Memutar suara SOS tiga kali
    for _ in range(3):
        print("\nSOS sound playing... Beep Beep Beep!")
        time.sleep(1)

    # Menampilkan kontak layanan kesehatan mental
    print("\n==== Mental Health Emergency Contacts ====")
    mental_health_contacts = {
        "Sejiwa Service (Ministry of Health of the Republic of Indonesia)": "119 ext. 8",
        "UGM Psychology Assistance": "0811-286-292",
        "Psychological Counseling Pijar Psychology": "0813-8830-0830",
        "Lifeline Indonesia": "021-2239-5700"
    }

    for service, number in mental_health_contacts.items():
        print(f"{service}: {number}")

    print("\nPlease reach out to these services if needed.")

if __name__ == "_main_":
    play_sos_and_display_contacts()