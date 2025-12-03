import argparse
import sys

DEFAULT_RATE = 6.34
DEFAULT_THRESHOLD = 300.0

def calculate_bill(previous_reading, current_reading, rate=DEFAULT_RATE, threshold=DEFAULT_THRESHOLD):
	prev = float(previous_reading)
	curr = float(current_reading)
	if prev < 0 or curr < 0:
		raise ValueError("Readings must be non-negative numbers.")
	if curr < prev:
		raise ValueError("Current reading must be greater than or equal to previous reading.")

	usage = curr - prev
	amount = usage * float(rate)
	return usage, amount, usage <= threshold


def format_currency(amount):
	return f"Rs {amount:,.2f}"


def main(argv=None):
	argv = argv if argv is not None else sys.argv[1:]
	parser = argparse.ArgumentParser(description="Electricity bill calculator")
	parser.add_argument("previous", nargs="?", type=float, help="Previous meter reading (3 months ago)")
	parser.add_argument("current", nargs="?", type=float, help="Current meter reading")
	parser.add_argument("--rate", type=float, default=DEFAULT_RATE, help=f"Rate per unit (default {DEFAULT_RATE})")
	parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD, help=f"Threshold units for no-bill (default {DEFAULT_THRESHOLD})")
	args = parser.parse_args(argv)

	try:
		if args.previous is None or args.current is None:
			prev = input("Enter previous meter reading (2 months ago)  : ").strip()
			curr = input("Enter current meter reading                  : ").strip()
			if prev == "" or curr == "":
				print("Both readings are required.")
				return 1
			previous = float(prev)
			current = float(curr)
		else:
			previous = args.previous
			current = args.current

		usage, amount, is_below_threshold = calculate_bill(previous, current, rate=args.rate, threshold=args.threshold)
	except ValueError as e:
		print(f"Input error: {e}")
		return 2

	print("\nElectricity bill summary")
	print("-----------------------------")
	print(f"Previous reading             : {previous}")
	print(f"Current reading              : {current}")
	print(f"Units used                   : {usage:.2f}")
	print(f"Threshold (no-bill if <=)    : {args.threshold:.2f} units")

	if is_below_threshold:
		print("Result                       : Below threshold - NO PAYMENT REQUIRED")
		print(f"Amount calculated            : {format_currency(amount)} (not to be paid)")
	else:
		print(f"Result                       : Above threshold - PAYMENT REQUIRED")
		print(f"Amount due                   : {format_currency(amount)}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())

  