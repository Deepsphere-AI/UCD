from math import sqrt, acos, degrees

class Triad:
    """
    Calculates angles and distances among a triad of points. Points can be supplied in any dimensional space,
    as long as they are consistent. Points are supplied as tuples in n-dimensions, and there should be three of
    those to make the triad. Each point is positionally named as p, q, r and the corresponding angles are then
    angleP, angleQ, and angleR. Distances are given by dPQ(), dPR(), and dQR().
    
    Attributes:
    p, q, r: The 3 tuples representing points in N-space
    
    Methods:
    angleQ(), angleP(), angleR(): Angles measured in degrees
    dPQ(), dPR(), dQR(): Distances in the same units of p, q, r
    """

    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r

    def d2(self, a, b):
        """Calculate squared distance of point a to b."""
        return sum((ia - ib) ** 2 for ia, ib in zip(a, b))

    def dot(self, a, b):
        """Dot product of standard vectors a and b."""
        return sum(ia * ib for ia, ib in zip(a, b))

    def ndot(self, a, b, c):
        """Dot Product of vector a, c standardized to b."""
        ab = [ia - ib for ia, ib in zip(a, b)]
        cb = [ic - ib for ic, ib in zip(c, b)]
        return sum(ia * ib for ia, ib in zip(ab, cb))

    def dPQ(self):
        """Provides the distance between point p and point q."""
        return sqrt(self.d2(self.p, self.q))

    def dPR(self):
        """Provides the distance between point p and point r."""
        return sqrt(self.d2(self.p, self.r))

    def dQR(self):
        """Provides the distance between point q and point r."""
        return sqrt(self.d2(self.q, self.r))

    def angleQ(self):
        """Provides the angle made at point q by segments qp and qr (degrees)."""
        return degrees(acos(self.ndot(self.p, self.q, self.r) / (self.dPQ() * self.dQR())))

    def angleP(self):
        """Provides the angle made at point p by segments pq and pr (degrees)."""
        return degrees(acos(self.ndot(self.q, self.p, self.r) / (self.dPQ() * self.dPR())))

    def angleR(self):
        """Provides the angle made at point r by segments rq and rp (degrees)."""
        return degrees(acos(self.ndot(self.q, self.r, self.p) / (self.dQR() * self.dPR())))

def main():
    coords_input = input("Enter three sets of atomic coordinates in the format 'C = (x, y, z) N = (x, y, z) Ca = (x, y, z)': \n")
    
    # Removing the labels and splitting based on the closing parenthesis
    coords_input = coords_input.replace("C = ", "").replace("N = ", "").replace("Ca = ", "")
    coords_list = coords_input.split(") ")
    
    # Parsing the coordinates while ensuring that spaces after commas are not mandatory
    coords = []
    for coord_str in coords_list:
        if coord_str:  # Check if the string is not empty
            clean_str = coord_str.strip("()")
            # Splitting by comma and ensuring each part is stripped of leading/trailing whitespaces
            parts = [part.strip() for part in clean_str.split(',')]
            coords.append(tuple(map(float, parts)))

    if len(coords) != 3:
        print("Error: Please enter exactly three sets of coordinates.")
        return

    triad = Triad(coords[1], coords[0], coords[2])  # Adjusted to the correct order: N, C, Ca

    # Calculating and displaying the results
    n_c_length = triad.dPQ()  # Distance between N and C
    n_ca_length = triad.dPR()  # Distance between N and Ca
    c_n_ca_angle = triad.angleP()  # Angle at N formed by C, N, and Ca
    
    print(f'N-C bond length = {n_c_length:.2f}')
    print(f'N-Ca bond length = {n_ca_length:.2f}')
    print(f'C-N-Ca bond angle = {c_n_ca_angle:.1f}')

if __name__ == "__main__":
    main()
