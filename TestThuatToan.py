import numpy as np


class Reference:
    reference = [
        {"left": 3764, "right": 2014},
        {"left": 6453, "right": 3890},
        {"left": 3890, "right": 2567},
        {"left": 3890, "right": 3214},
        {"left": 3890, "right": 2098},
        {"left": 3214, "right": 2098},
        {"left": 3890, "right": 3222},
        {"left": 3890, "right": 2098},
        {"left": 3214, "right": 4245},
    ]

    @classmethod
    def count_left_occurrences(cls):
        left_counts = {}
        for item in cls.reference:
            left_value = item["left"]
            left_counts[left_value] = left_counts.get(left_value, 0) + 1
        return left_counts

    @classmethod
    def create_left_matrix(cls):
        # Tạo danh sách chứa tất cả các giá trị left
        left_values = [item["left"] for item in cls.reference]

        # Loại bỏ các giá trị trùng lặp và sắp xếp lại
        unique_left_values = sorted(set(left_values))

        # Tạo ma trận kích thước len(unique_left_values) x len(unique_left_values) với giá trị ban đầu là 0
        matrix = np.zeros((len(unique_left_values), len(unique_left_values)))

        # Duyệt qua danh sách data và cập nhật ma trận dựa trên left và số lần xuất hiện chia cho 1
        left_counts = cls.count_left_occurrences()
        for item in cls.reference:
            left_value = item["left"]
            left_index = unique_left_values.index(left_value)
            matrix[left_index][left_index] = 1 / left_counts[left_value]

        return matrix


    @classmethod
    def print_left_right_values(cls):
        seen_values = []
        for item in cls.reference:
            left_value = item.get("left")
            right_value = item.get("right")
            if left_value == right_value:
                print(f"left: {left_value}")
            else:
                if (left_value, right_value) not in seen_values:
                    print(f"left: {left_value}, right: {right_value}")
                    seen_values.append((left_value, right_value))
    @classmethod
    def get_unique_left_values(cls):
        # Tạo danh sách chứa tất cả các giá trị left
        left_values = [item["left"] for item in cls.reference]
        # Loại bỏ các giá trị trùng lặp và sắp xếp lại
        unique_left_values = sorted(set(left_values))
        return unique_left_values

if __name__ == "__main__":
    # Tạo ma trận dựa trên giá trị của left và số lần xuất hiện của left
    left_matrix = Reference.create_left_matrix()
    print("\nMa trận dựa trên giá trị của left và 1 chia cho số lần xuất hiện của left:")
    unique_left_values = Reference.get_unique_left_values()
    for i in range(len(unique_left_values)):
        left_value = unique_left_values[i]
        for j in range(len(unique_left_values)):
            print(f"Giá trị tương ứng với {left_value}: {left_matrix[i][j]}")

        # Tạo ma trận dựa trên giá trị của left và số lần xuất hiện của left
        matrix = Reference.create_left_matrix()

        # In ma trận ra màn hình
        print(matrix)
    # In số lần xuất hiện của từng left ID
    left_counts = Reference.count_left_occurrences()
    print("\nSố lần xuất hiện của từng left ID:")
    for left_value, count in left_counts.items():
        print(f"ID: {left_value}, Số lần xuất hiện: {count}")

    # In giá trị của left và right
    print("\nGiá trị của left và right:")
    Reference.print_left_right_values()





