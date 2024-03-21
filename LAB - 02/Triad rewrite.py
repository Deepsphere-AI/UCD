import math

class Triad:
    def __init__(self, p, q, r):
        """
        Construct a Triad with points p, q, and r.

        Example object construction:
        p1 = Triad(p=(1., 0., 0.), q=(0., 0., 0.), r=(0., 0., 0.))
        """
        self.p = p
        self.q = q
        self.r = r

    def dPQ(self):
        """Return the distance between point p and point q."""
        return math.sqrt(sum((self.p[i] - self.q[i])**2 for i in range(3)))

    def dPR(self):
        """Return the distance between point p and point r."""
        return math.sqrt(sum((self.p[i] - self.r[i])**2 for i in range(3)))

    def dQR(self):
        """Return the distance between point q and point r."""
        return math.sqrt(sum((self.q[i] - self.r[i])**2 for i in range(3)))

    def angleP(self):
        """Return the angle made at point p by segments pq and pr."""
        pq = self.dPQ()
        pr = self.dPR()
        qr = self.dQR()
        return math.degrees(math.acos((pq**2 + pr**2 - qr**2) / (2 * pq * pr)))

    def angleQ(self):
        """Return the angle made at point q by segments qp and qr."""
        pq = self.dPQ()
        qr = self.dQR()
        pr = self.dPR()
        return math.degrees(math.acos((pq**2 + qr**2 - pr**2) / (2 * pq * qr)))

    def angleR(self):
        """Return the angle made at point r by segments rp and rq."""
        pr = self.dPR()
        qr = self.dQR()
        pq = self.dPQ()
        return math.degrees(math.acos((pr**2 + qr**2 - pq**2) / (2 * pr * qr)))

# Example usage
if __name__ == "__main__":
    triad = Triad(p=(1., 0., 0.), q=(0., 0., 0.), r=(0., 0., 1.))
    print("Distance PQ:", triad.dPQ())
    print("Distance PR:", triad.dPR())
    print("Distance QR:", triad.dQR())
    print("Angle at P:", triad.angleP())
    print("Angle at Q:", triad.angleQ())
    print("Angle at R:", triad.angleR())
