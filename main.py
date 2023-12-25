import psutil
import customtkinter as ctk

ctk.set_appearance_mode("dark")

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitor")
        # Make the window always stay on top
        self.root.wm_attributes("-topmost", True)
        # hide the menubar
        self.root.overrideredirect(True)


        # Labels for displaying system information
        self.cpu_label = ctk.CTkLabel(root, text="CPU:")
        self.cpu_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.cpu_usage = ctk.CTkLabel(root, text="")
        self.cpu_usage.grid(row=0, column=1, padx=1, pady=5, sticky="w")

        self.ram_label = ctk.CTkLabel(root, text="RAM:")
        self.ram_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.ram_usage = ctk.CTkLabel(root, text="")
        self.ram_usage.grid(row=0, column=3, padx=1, pady=5, sticky="w")

        self.disk_label = ctk.CTkLabel(root, text="DISK:")
        self.disk_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        
        self.disk_usage = ctk.CTkLabel(root, text="")
        self.disk_usage.grid(row=0, column=5, padx=1, pady=5, sticky="w")

        self.network_label = ctk.CTkLabel(root, text="NET:")
        self.network_label.grid(row=0, column=6, padx=5, pady=5, sticky="w")

        self.network_usage = ctk.CTkLabel(root, text="")
        self.network_usage.grid(row=0, column=7, padx=1, pady=5, sticky="w")

        self.center_top()
        self.update_stats()

    def center_top(self):
        screen_width = self.root.winfo_screenwidth()
        # screen_height = self.root.winfo_screenheight()

        window_width = 530
        window_height = 40

        x = (screen_width - window_width) // 2

        self.root.geometry(f"{int(window_width)}x{int(window_height)}+{x}+0")

    def update_stats(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        num_cpus = psutil.cpu_count()
        self.cpu_usage.configure(text=f"{cpu_percent:.0f}%  (Num: {num_cpus})")

        ram_percent = psutil.virtual_memory().percent
        self.ram_usage.configure(text=f"{ram_percent:.0f}%")

        disk_percent = psutil.disk_usage("/").percent
        self.disk_usage.configure(text=f"{disk_percent:.0f}%")

        network_info = psutil.net_io_counters()
        sent = network_info.bytes_sent
        received = network_info.bytes_recv
        self.network_usage.configure(text=f"Sent: {sent / 1024:.2f} KB   Received: {received / 1024:.2f} KB")

        self.root.after(1000, self.update_stats)

if __name__ == "__main__":
    root = ctk.CTk()
    app = SystemMonitorApp(root)
    root.mainloop()
