


# 'Theater' 부모 클래스를 정의한다.
class Theater:
    # 'Theater' 클래스는 영화관의 이름을 저장하는 'name' 인스턴스 변수를 가진다.
    # 'Theater' 클래스는 영화관의 총 좌석 수를 저장하는 'total_seats' 인스턴스 변수를 가진다.
    # 'Theater' 클래스는 현재 예약된 좌석 수를 저장하는 'reserved_seats' 인스턴스 변수를 가진다.
    def __init__(self, name, total_seats, reserved_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = reserved_seats

    # 'Theater' 클래스는 좌석을 예약하는 'reserve_seat' 인스턴스 메서드를 가진다.
        # 'reserve_seat' 메서드는 예약 가능한 좌석이 있는 경우, 'reserved_seats'를 1 증가시키고 예약 성공 메시지를 반환한다.
        # 예약 가능한 좌석이 없는 경우, 예약 실패 메시지를 반환한다.
    def reserve_seat(self):
        if self.total_seats > self.reserved_seats:
            self.reserved_seats += 1
            print("좌석 예약이 완료되었습니다.")
        else:
            print("예약 실패")
    
# MovieTheater 자식 클래스를 정의하고, Theater 클래스를 상속받는다.
class MovieTheater(Theater):
    # MovieTheater 클래스는 영화관의 총 영화 수를 저장하는 total_movies 클래스 변수를 가진다.
    total_movies = 0

    # MovieTheater 클래스는 영화관의 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다.
        # add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        return "영화가 추가되었습니다."

    # MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
        # description 메서드는 영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 출력한다.
    @staticmethod
    def description(instance):
        print(f"영화관 이름: {instance.name}")
        print(f"총 좌석 수: {instance.total_seats}")
        print(f"예약된 좌석 수: {instance.reserved_seats}")
        print(f"총 영화 수: {MovieTheater.total_movies}")

Theater1 = Theater('메가박스', 100, 0)
MovieTheater.add_movie()
Theater1.reserve_seat()
Theater1.reserve_seat()
MovieTheater.description(Theater1)
