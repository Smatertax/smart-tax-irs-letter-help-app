
import streamlit as st

st.set_page_config(page_title="Smart Tax – IRS Letter Help (CP504)")

st.title("📬 IRS CP504 or Collection Letter Received?")
st.markdown("We’re here to help you understand what it means and what you can do next.")

# Input
st.subheader("What letter did you receive?")
letter_type = st.selectbox("Select IRS Letter", ["CP504", "CP14", "CP90", "LT11", "Other"])

owed_amount = st.number_input("Amount the IRS says you owe ($)", min_value=0)

action_taken = st.selectbox("Have you responded to the IRS yet?", ["No", "Yes – I called them", "Yes – I sent documents", "Yes – I paid"])

st.subheader("What’s your biggest concern?")
concern = st.radio("Choose one:", [
    "I don’t understand what the letter means",
    "I can’t afford to pay what they’re asking",
    "I want to stop wage garnishment or liens",
    "I want to settle for less than I owe",
    "I need help avoiding further penalties"
])

# Output logic
if st.button("Show My Options"):
    st.markdown("---")
    st.subheader("🧾 What This Letter Means")

    if letter_type == "CP504":
        st.write("CP504 is a **Final Notice** from the IRS stating they plan to levy (take) your **state tax refund** or other assets if you don’t respond.")
        st.warning("⚠️ This is serious. You must act within 30 days to avoid further action.")

    elif letter_type == "CP14":
        st.write("CP14 is the first notice the IRS sends when you owe a balance. It includes the amount owed and due date.")
        st.info("💡 You may be eligible for a payment plan before penalties increase.")

    elif letter_type == "CP90" or letter_type == "LT11":
        st.write("This letter means the IRS **intends to levy your property or wages.**")
        st.error("🛑 Immediate action is needed. You may qualify for a Collection Due Process hearing.")

    else:
        st.write("This is likely an early collection or adjustment notice. We recommend having it reviewed by a tax pro.")

    st.markdown("### ✅ Your Next Steps")

    if action_taken == "No":
        st.write("• Call the IRS or respond by the deadline listed in your letter.")
        st.write("• Keep records of all communications.")
        st.write("• If you can’t pay in full, request a payment plan or Offer in Compromise.")

    elif action_taken == "Yes – I called them":
        st.write("• Keep a log of who you spoke with and what was said.")
        st.write("• If no resolution was reached, consider getting professional representation.")

    elif action_taken == "Yes – I paid":
        st.write("• Confirm that the payment was received and processed.")
        st.write("• Request an account transcript to verify no further action is needed.")

    else:
        st.write("• Follow up with any documents or proof you submitted.")
        st.write("• If the IRS does not respond within 30 days, call them or consult a tax pro.")

    st.markdown("### 🧠 Based on your concern:")

    if concern == "I don’t understand what the letter means":
        st.info("✅ Let Smart Tax interpret the letter for you and explain what it means in plain English.")

    elif concern == "I can’t afford to pay what they’re asking":
        st.warning("You may qualify for **Hardship**, **Non-Collectible** status, or an **Offer in Compromise.**")

    elif concern == "I want to stop wage garnishment or liens":
        st.error("You must act quickly. Smart Tax can help file for Collection Due Process or apply for a stay.")

    elif concern == "I want to settle for less than I owe":
        st.success("You may be a candidate for the **IRS Offer in Compromise** program. We can help file it.")

    elif concern == "I need help avoiding further penalties":
        st.info("Responding fast helps reduce penalties. We can help you file appeals or payment relief forms.")

    st.markdown("---")
    st.subheader("📞 Ready for Relief?")
    st.markdown("Smart Tax specializes in resolving IRS letters fast. Let us help you take the next step.")
    st.link_button("🧾 Book a Free IRS Letter Review Call", "https://calendly.com/smarttax/irs-letter-help")
    st.markdown("Or DM us on Instagram: [@smartertxs](https://instagram.com/smartertxs)")

st.markdown("---")
st.caption("Smart Tax – Trusted help for taxpayers dealing with the IRS. #SmarterNotHarder")
