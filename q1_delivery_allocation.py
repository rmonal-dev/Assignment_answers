"""
Group 1 - Question 5
Delivery Allocation Module — Round Robin Assignment

Description:
    Simulates a food delivery system where orders are assigned to active
    delivery partners in a round-robin manner. Partners can come online
    or go offline dynamically, and orders are only assigned to active ones.
"""

from collections import deque


class DeliveryAllocationSystem:
    """
    Manages delivery partners and assigns incoming orders
    using a Round Robin scheduling strategy.
    """

    def __init__(self):
        # Tracks all partners and their status
        self.partners: dict[str, bool] = {}          # name -> is_active
        self.active_queue: deque[str] = deque()      # circular queue of active partners
        self.order_log: list[dict] = []              # history of all assignments
        self.delivery_count: dict[str, int] = {}     # total deliveries per partner

    # ------------------------------------------------------------------ #
    #  Partner Management                                                  #
    # ------------------------------------------------------------------ #

    def partner_online(self, name: str) -> None:
        """Bring a delivery partner online."""
        if name in self.partners and self.partners[name]:
            print(f"  [INFO] {name} is already online.")
            return

        self.partners[name] = True
        self.active_queue.append(name)
        if name not in self.delivery_count:
            self.delivery_count[name] = 0
        print(f"    {name} is now ONLINE  |  Active partners: {list(self.active_queue)}")

    def partner_offline(self, name: str) -> None:
        """Take a delivery partner offline."""
        if name not in self.partners or not self.partners[name]:
            print(f"  [INFO] {name} is already offline or unknown.")
            return

        self.partners[name] = False
        # Rebuild queue without the departing partner
        self.active_queue = deque(p for p in self.active_queue if p != name)
        print(f"    {name} went OFFLINE    |  Active partners: {list(self.active_queue)}")

    # ------------------------------------------------------------------ #
    #  Order Assignment                                                    #
    # ------------------------------------------------------------------ #

    def assign_order(self, order_id: str) -> str | None:
        """
        Assign an order to the next available partner (round robin).
        Returns the assigned partner's name, or None if no one is available.
        """
        if not self.active_queue:
            print(f"    Order {order_id}: No active delivery partners available!")
            return None

        # Take from front → append to back (circular)
        partner = self.active_queue.popleft()
        self.active_queue.append(partner)

        self.delivery_count[partner] += 1
        self.order_log.append({"order_id": order_id, "assigned_to": partner})
        print(f"    Order {order_id:>6}  →  Assigned to: {partner:<15} (total: {self.delivery_count[partner]})")
        return partner

    # ------------------------------------------------------------------ #
    #  Reporting                                                           #
    # ------------------------------------------------------------------ #

    def print_summary(self) -> None:
        """Display a summary of all deliveries."""
        print("\n" + "=" * 55)
        print("         DELIVERY ALLOCATION SUMMARY")
        print("=" * 55)
        print(f"  Total orders assigned : {len(self.order_log)}")
        print(f"  Active partners now   : {list(self.active_queue) or 'None'}")
        print()
        print(f"  {'Partner':<20} {'Deliveries':>10}  {'Bar'}")
        print(f"  {'-'*20}  {'-'*10}  {'-'*15}")
        for partner, count in sorted(self.delivery_count.items(), key=lambda x: -x[1]):
            bar = "█" * count
            status = "🟢" if self.partners.get(partner) else "🔴"
            print(f"  {status} {partner:<18} {count:>10}  {bar}")
        print("=" * 55)


# ------------------------------------------------------------------ #
#  Demo / Driver                                                       #
# ------------------------------------------------------------------ #

def main():
    print("\n" + "=" * 55)
    print("    Food Delivery — Round Robin Allocation Demo")
    print("=" * 55)

    system = DeliveryAllocationSystem()

    # --- Phase 1: Three partners come online ---
    print("\n[Phase 1] Partners coming online")
    system.partner_online("Ravi")
    system.partner_online("Priya")
    system.partner_online("Arjun")

    # --- Phase 2: Assign first 6 orders ---
    print("\n[Phase 2] Assigning orders #1 – #6")
    for i in range(1, 7):
        system.assign_order(f"ORD-{i:03}")

    # --- Phase 3: One partner goes offline ---
    print("\n[Phase 3] Priya goes offline")
    system.partner_offline("Priya")

    # --- Phase 4: Assign next 4 orders (only Ravi & Arjun active) ---
    print("\n[Phase 4] Assigning orders #7 – #10  (2 active partners)")
    for i in range(7, 11):
        system.assign_order(f"ORD-{i:03}")

    # --- Phase 5: New partner joins ---
    print("\n[Phase 5] Meena comes online")
    system.partner_online("Meena")

    # --- Phase 6: Assign 3 more orders ---
    print("\n[Phase 6] Assigning orders #11 – #13")
    for i in range(11, 14):
        system.assign_order(f"ORD-{i:03}")

    # --- Phase 7: All partners offline, order arrives ---
    print("\n[Phase 7] All partners go offline")
    system.partner_offline("Ravi")
    system.partner_offline("Arjun")
    system.partner_offline("Meena")
    system.assign_order("ORD-014")   # Should warn: no partners

    # --- Summary ---
    system.print_summary()


if __name__ == "__main__":
    main()
