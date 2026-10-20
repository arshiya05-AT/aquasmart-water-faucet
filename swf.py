import streamlit as st
import time
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=1000, key="water_refresh")

st.set_page_config(
    page_title="Smart Water Faucet",
    page_icon="💧",
    layout="wide"
)

if "faucet_on" not in st.session_state:
    st.session_state.faucet_on = False
if "water_used" not in st.session_state:
    st.session_state.water_used = 0.0
if "water_saved" not in st.session_state:
    st.session_state.water_saved = 0.0
if "activity_history" not in st.session_state:
    st.session_state.activity_history = []
if "last_update" not in st.session_state:
    st.session_state.last_update = time.time()

current_time = time.time()
elapsed = current_time - st.session_state.last_update

if st.session_state.faucet_on:
    st.session_state.water_used += elapsed * 0.02

st.session_state.last_update = current_time
st.markdown("""
<style>
.stApp { background-color: #F3F7FC; }
[data-testid="stSidebar"] { background-color: #10243A; }
[data-testid="stSidebar"] * { color: white; }
.hero {
    background: linear-gradient(120deg, #10243A, #087EAD);
    padding: 28px;
    border-radius: 18px;
    color: white;
    margin-bottom: 24px;
}
.hero h1 { color: white; font-size: 32px; }
.hero p { color: #E0F2FE; }
.metric {
    background: white;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #DFE8F2;
}
.metric-label { color: #62748A; font-size: 13px; }
.metric-value {
    color: #10243A;
    font-size: 27px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("# 💧 AquaSmart")
    st.caption("SMART WATER MANAGEMENT")
    st.divider()
    page = st.radio(
        "NAVIGATION",
        ["Dashboard", "Automatic Faucet", "Water Analytics", "Activity History"]
    )
    st.divider()
    st.caption("SOFTWARE SIMULATION")

st.markdown("""
<div class="hero">
    <h1>Smart Automatic Water Faucet</h1>
    <p>Touchless faucet simulation and intelligent water monitoring.</p>
</div>
""", unsafe_allow_html=True)

status = "ON" if st.session_state.faucet_on else "OFF"

a, b, c = st.columns(3)

with a:
    st.markdown(f"""
    <div class="metric">
        <div class="metric-label">FAUCET STATUS</div>
        <div class="metric-value">{status}</div>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown(f"""
    <div class="metric">
        <div class="metric-label">WATER CONSUMED</div>
        <div class="metric-value">{st.session_state.water_used:.2f} L</div>
    </div>
    """, unsafe_allow_html=True)

with c:
    saved_value = st.session_state.water_saved
    st.markdown(
        f"""
        <div class="metric">
            <div class="metric-label">WATER SAVED</div>
            <div class="metric-value">{saved_value:.2f} L</div>
        </div>
        """,
        unsafe_allow_html=True
    )
st.divider()

if page == "Dashboard":
    st.subheader("System Overview")
    if st.session_state.faucet_on:
        st.success("🟢 System Active — Faucet is ON")
    else:
        st.info("⚪ System Ready — Faucet is OFF")

    st.write(
        "AquaSmart simulates touchless water control "
        "and tracks water consumption and estimated savings."
    )
    st.divider()
    st.subheader("💧 How AquaSmart Works")

    st.markdown("""
    1. **Hand Detection:** Simulates detecting a hand near the faucet.
    2. **Automatic Water Control:** Turns the simulated faucet ON or OFF.
    3. **Water Monitoring:** Tracks estimated water consumption.
    4. **Water Saving:** Displays illustrative water-saving estimates.
    5. **Water Analytics:** Shows a chart comparing water consumed and saved.
    """)
    st.divider()
    st.subheader("📘 About This Project")

    st.write(
        "AquaSmart is a Python-based software simulation "
        "of an automatic water faucet. It demonstrates "
        "touchless faucet control, water consumption "
        "monitoring, and estimated water savings."
    )

    st.caption(
        "Technology Used: Python • Streamlit • VS Code"
    )
    st.divider()
    st.subheader("🌱 Water-Saving Tip")

    st.info(
        "Turn off the faucet when it is not needed. "
        "Automatic faucet systems can help reduce "
        "unnecessary water usage."
    )
    st.divider()
    st.subheader("🔄 Reset Simulation")

    if st.button("Reset All Values", type="secondary"):
        st.session_state.faucet_on = False
        st.session_state.water_used = 0.0
        st.session_state.water_saved = 0.0
        st.session_state.activity_history = []
        st.session_state.last_update = time.time()
        st.rerun()
    if st.session_state.faucet_on:
        st.success("Water is flowing in simulation.")
    else:
        st.info("Faucet is OFF and ready for hand detection.")
        st.write("Use the Automatic Faucet page to control the simulation.")

elif page == "Automatic Faucet":
    st.subheader("Automatic Faucet Control")
    st.write("Simulate a hand moving near the sensor.")

    if st.session_state.faucet_on:
        st.success("🟢 Hand detected — Faucet is ON")

        if st.button("✋ Remove Hand — Turn OFF", type="primary"):
            st.session_state.faucet_on = False
            st.session_state.water_saved += 0.20
            st.session_state.activity_history.append({
                "Time": time.strftime("%Y-%m-%d %H:%M:%S"),
                "Activity": "Faucet turned OFF",
                "Water Used (L)": round(st.session_state.water_used, 2)
            })
            st.session_state.last_update = time.time()
            st.rerun()

    else:
        st.info("⚪ No hand detected — Faucet is OFF")

        if st.button("🖐 Detect Hand — Turn ON", type="primary"):
            st.session_state.faucet_on = True
            st.session_state.activity_history.append({
                "Time": time.strftime("%Y-%m-%d %H:%M:%S"),
                "Activity": "Faucet turned ON",
                "Water Used (L)": round(st.session_state.water_used, 2)
            })
            st.rerun()

    st.caption(
        "This is a software simulation; no physical sensor or valve is connected."
    )
elif page == "Water Analytics":
    st.subheader("Water Analytics")
    st.write("Monitor simulated water consumption and savings.")
    st.divider()
    st.subheader("🎯 Daily Water Usage Goal")

    daily_goal = st.number_input(
        "Set your water usage target (litres)",
        min_value=1.0,
        max_value=100.0,
        value=10.0,
        step=1.0
    )

    water_used = st.session_state.water_used

    st.progress(
        min(water_used / daily_goal, 1.0)
    )

    st.write(
        f"Water used: {water_used:.2f} L / "
        f"{daily_goal:.2f} L"
    )

    if water_used <= daily_goal:
        st.success("You are within your water usage goal!")
    else:
        st.warning("Your water usage has exceeded the goal.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Water Consumed",
            f"{st.session_state.water_used:.2f} L"
        )

    with col2:
        st.metric(
            "Total Water Saved",
            f"{st.session_state.water_saved:.2f} L"
        )

    st.divider()
    st.subheader("Water Usage Comparison")

    chart_data = {
        "Category": ["Water Consumed", "Water Saved"],
        "Litres": [
            st.session_state.water_used,
            st.session_state.water_saved
        ]
    }

    st.bar_chart(
        chart_data,
        x="Category",
        y="Litres",
        color="#087EAD"
    )

    st.caption(
        "Note: Values are illustrative software-simulation estimates, "
        "not measurements from a physical sensor."
    )

elif page == "Activity History":
    st.subheader("Activity History")
    st.write("View and download your faucet activity records.")

    if st.session_state.activity_history:
        import pandas as pd

        history_df = pd.DataFrame(
            st.session_state.activity_history
        )

        csv_data = history_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Activity Report",
            data=csv_data,
            file_name="aquasmart_activity_report.csv",
            mime="text/csv"
        )

        st.dataframe(history_df, use_container_width=True)

    else:
        st.info("No activity recorded yet. Visit Automatic Faucet to begin.")
    st.write("Records of faucet activity")

    if st.session_state.activity_history:
        st.dataframe(
            st.session_state.activity_history,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No activity recorded yet. Visit Automatic Faucet to begin.")
st.divider()
st.caption("AquaSmart | Smart Automatic Water Faucet | Software Prototype")
st.markdown(
    """
    <div style="text-align:center; padding:20px; color:#64748b;">
        <hr>
        <p><b>AquaSmart</b> — Smart Automatic Water Faucet Monitoring System</p>
        <p>Built with Python and Streamlit | Academic Project — 2026</p>
        <p>💧 Save Water, Save Life</p>
    </div>
    """,
    unsafe_allow_html=True
)