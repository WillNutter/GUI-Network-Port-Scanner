import socket
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from threading import Thread


def scan_ports(ip, start_port, end_port, output_widget):
    output_widget.delete("1.0", tk.END)
    open_ports = []

    try:
        ip = socket.gethostbyname(ip)
    except socket.gaierror:
        output_widget.insert(tk.END, f"Invalid IP address or hostname: {ip}\n")
        return

    output_widget.insert(tk.END, f"Scanning {ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
                    output_widget.insert(tk.END, f"[+] Port {port} is OPEN\n")
                else:
                    output_widget.insert(tk.END, f"[-] Port {port} is closed\n")
        except Exception as e:
            output_widget.insert(tk.END, f"Error scanning port {port}: {e}\n")

    output_widget.insert(tk.END, f"\nScan complete. {len(open_ports)} open ports found.\n")


def start_scan():
    ip = ip_entry.get()
    try:
        start_port = int(start_entry.get())
        end_port = int(end_entry.get())
        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535 and start_port <= end_port):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Port Range", "Ports must be integers between 0 and 65535.")
        return

    thread = Thread(target=scan_ports, args=(ip, start_port, end_port, output_text))
    thread.start()


# GUI setup
root = tk.Tk()
root.title("Python Port Scanner")
root.geometry("600x400")

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Target IP/Hostname:").grid(row=0, column=0, sticky=tk.W)
ip_entry = ttk.Entry(frame, width=30)
ip_entry.grid(row=0, column=1, sticky=tk.W)

ttk.Label(frame, text="Start Port:").grid(row=1, column=0, sticky=tk.W)
start_entry = ttk.Entry(frame, width=10)
start_entry.grid(row=1, column=1, sticky=tk.W)

ttk.Label(frame, text="End Port:").grid(row=2, column=0, sticky=tk.W)
end_entry = ttk.Entry(frame, width=10)
end_entry.grid(row=2, column=1, sticky=tk.W)

scan_button = ttk.Button(frame, text="Scan", command=start_scan)
scan_button.grid(row=3, column=0, columnspan=2, pady=10)

output_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=70, height=15)
output_text.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
