import streamlit as st

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Công Cụ Tính Lãi Tiết Kiệm Ngân Hàng_Phạm Thuỳ Mỹ Duyên",
    page_icon="🏦",
    st.image("logo.jpg")   
    layout="centered"

st.title("🏦 Công Cụ Tính Lãi Gửi Tiết Kiệm Ngân Hàng_Phạm Thuỳ Mỹ Duyên")
st.write("Nhập các thông tin bên dưới để tính toán tiền lãi dự kiến nhận được.")

st.divider()

# --- KHU VỰC NHẬP DỮ LIỆU ---
col1, col2 = st.columns(2)

with col1:
    so_tien_gui = st.number_input(
        "Số tiền gửi (VNĐ):",
        min_value=1_000_000,
        value=100_000_000,
        step=5_000_000,
        format="%d"
    )
    
    ky_han_thang = st.number_input(
        "Kỳ hạn gửi (tháng):",
        min_value=1,
        max_value=60,
        value=12,
        step=1
    )

with col2:
    lai_suat_nam = st.number_input(
        "Lãi suất (%/năm):",
        min_value=0.1,
        max_value=20.0,
        value=5.5,
        step=0.1,
        format="%.2f"
    )

    hinh_thuc_tra_lai = st.selectbox(
        "Hình thức nhận lãi:",
        options=["Cuối kỳ", "Hàng tháng", "Hàng quý"]
    )

# --- TÍNH TOÁN KẾT QUẢ ---
# Công thức chuẩn ngân hàng: Lãi năm = (Số tiền * Lãi suất%/năm)

if hinh_thuc_tra_lai == "Cuối kỳ":
    # Lãi cuối kỳ nhận 1 lần khi đáo hạn
    tong_tien_lai = so_tien_gui * (lai_suat_nam / 100) * (ky_han_thang / 12)
    tien_lai_dinh_ky = tong_tien_lai
    chu_ky_nhan = "vào cuối kỳ"

elif hinh_thuc_tra_lai == "Hàng tháng":
    # Lãi hàng tháng = (Số tiền * Lãi suất / 12)
    tien_lai_dinh_ky = so_tien_gui * (lai_suat_nam / 100) / 12
    tong_tien_lai = tien_lai_dinh_ky * ky_han_thang
    chu_ky_nhan = "mỗi tháng"

elif hinh_thuc_tra_lai == "Hàng quý":
    # Lãi hàng quý (mỗi quý = 3 tháng)
    so_quy = ky_han_thang / 3
    tien_lai_dinh_ky = so_tien_gui * (lai_suat_nam / 100) * (3 / 12)
    tong_tien_lai = tien_lai_dinh_ky * so_quy
    chu_ky_nhan = "mỗi quý (3 tháng)"

tong_goc_va_lai = so_tien_gui + tong_tien_lai

st.divider()

# --- HIỂN THỊ KẾT QUẢ ---
st.subheader("📊 Kết Quả Dự Tính")

# Định dạng hiển thị tiền VNĐ
def format_vnd(amount):
    return f"{amount:,.0f} VNĐ".replace(",", ".")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        label=f"Lãi định kỳ ({chu_ky_nhan})",
        value=format_vnd(tien_lai_dinh_ky)
    )

with m2:
    st.metric(
        label="Tổng tiền lãi",
        value=format_vnd(tong_tien_lai)
    )

with m3:
    st.metric(
        label="Tổng gốc + lãi",
        value=format_vnd(tong_goc_va_lai)
    )

# Cảnh báo nhỏ nếu chọn nhận lãi hàng quý nhưng kỳ hạn không chia hết cho 3
if hinh_thuc_tra_lai == "Hàng quý" and ky_han_thang % 3 != 0:
    st.warning("⚠️ Lưu ý: Kỳ hạn gửi không chia hết cho 3 tháng. Kết quả tính theo tỷ lệ chính xác của kỳ hạn.")

st.info("📌 *Ghi chú: Kết quả trên mang tính chất tham khảo. Lãi thực tế có thể chênh lệch nhỏ tùy theo số ngày thực tế trong tháng/năm của từng ngân hàng.*")
