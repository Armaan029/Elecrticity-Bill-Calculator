# ⚡ Electricity Bill Calculator

Command-line electricity bill calculator for Indian households. Calculates charges based on slab-wise tariff rates (0-100 units, 101-200 units, 200+ units) with fixed charges, taxes, and total payable amount. Perfect for engineering students learning conditional logic and real-world applications. [web:30][web:32][web:34]

## ✨ Features
- **Slab-wise pricing**: 0-100 (₹4/unit), 101-200 (₹6/unit), 200+ (₹8/unit)
- **Fixed charges**: ₹100/month + 10% electricity duty
- **Input validation**: Handles invalid units and edge cases
- **Detailed breakdown**: Unit-wise charges, tax, and total
- **Real-world Indian tariff structure**

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Libraries**: Built-in (`math` for rounding)

## 📊 Sample Tariff (India Domestic)
| Units Consumed | Rate per Unit | Fixed Charge |
|----------------|---------------|--------------|
| 0-100          | ₹4.00         | ₹100         |
| 101-200        | ₹6.00         | ₹100         |
| 200+           | ₹8.00         | ₹100         |
*+10% Electricity Duty on total*

## 🚀 Getting Started

### Prerequisites
- Python 3.6+

### Installation


## 💻 Sample Code Structure
def calculate_bill(units):
if units <= 100:
return units * 4 + 100 + (units * 4 * 0.1)
# ... slab logic


## 🎓 Learning Outcomes
- Conditional statements (if-elif-else)
- Mathematical calculations with rounding
- Formatted output and tables
- Real-world problem solving
- Input validation and error handling

## 🤝 Contributing
1. Fork the repo
2. Create feature branch (`git checkout -b feature/add-new-slab`)
3. Commit changes (`git commit -m 'Add new tariff slab'`)
4. Push to branch (`git push origin feature/add-new-slab`)
5. Open Pull Request

## 📄 License
MIT License - see [LICENSE](LICENSE) file.

## 🙏 Acknowledgments
- Built for LPU Engineering students
- Indian electricity board tariff structure
- Standard GitHub portfolio practices [web:21]
