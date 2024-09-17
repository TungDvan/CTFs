import java.util.*;

public class Flag_Checker {
	static int[] pos = { 10, 15, 19, 28, 30, 44, 49 };
	static int[] f1nal = { 18, 20, 22, 23, 25, 26, 27, 31, 33, 34, 36, 37, 39, 40 };

	public static boolean check(boolean ret, String s) {
		if ((!s.substring(0, 5).equals("KCSC{")) || !(s.charAt(s.length() - 1) == '}'))
			ret = false;
		return ret;
	}

	public static boolean check(boolean ret, String s, int[] arr) {
		for (int i = 0; i < arr.length; ++i) {
			if (s.charAt(arr[i]) != 95)
				return false;
		}
		return ret;
	}

	public static boolean check(boolean ret, String s, boolean[] arr) {
		int[] num = new int[10];

		for (int i = 0; i < s.length(); ++i) {
			if (Character.isDigit(s.charAt(i)) != arr[i])
				ret = false;
		}
		for (int i = 0; i < pos.length; ++i) {
			num[i] = s.charAt(pos[i]) - 0x30;
		}
		if ((num[1] != num[6])
				|| (num[0] != num[1] - num[6])
				|| (num[3] + num[4] != num[1])
				|| (num[6] * num[5] != 20)
				|| (num[0] != num[2])
				|| (Math.pow(num[3], num[5]) != 256)
				|| ((num[1] ^ num[4]) != 4)
				|| (num[1] != 5)) {
			ret = false;
		}
		return ret;
	}
	


	public static boolean check(boolean ret, String s, char[] arr) {
		int l = 5, r = 55, cnt = 0;
		while (cnt < arr.length) {
			while (!Character.isLetter(s.charAt(l)))
				l++;
			while (!Character.isLetter(s.charAt(r)))
				r--;
			if (s.charAt(r) != arr[cnt] || s.charAt(l) != arr[cnt + 1]) {
				ret = false;
			}
			cnt += 2;
			l++;
			r--;
		}
		return ret;
	}

	public static boolean check(boolean ret, String s, String tmp) {
		for (int i = 0; i < f1nal.length; ++i)
			tmp += s.charAt(f1nal[i]);

		if (((tmp.charAt(2) ^ tmp.charAt(0)) != 32)
				|| (tmp.charAt(0) + tmp.charAt(5) + tmp.charAt(6) != 294)
				|| (tmp.charAt(1) * tmp.charAt(3) != 8160)
				|| ((tmp.charAt(3) ^ tmp.charAt(4)) != 44)
				|| ((tmp.charAt(2) ^ tmp.charAt(3)) != 9)
				|| (tmp.charAt(0) * tmp.charAt(3) != 8058)
				|| (tmp.charAt(3) - tmp.charAt(4) != 28)
				|| ((tmp.charAt(2) ^ tmp.charAt(7)) != 28)
				|| (tmp.charAt(12) - tmp.charAt(13) + tmp.charAt(9) - tmp.charAt(8) != 38)
				|| (tmp.charAt(3) - tmp.charAt(4) != 28)
				|| ((tmp.charAt(2) ^ tmp.charAt(11)) != 0)
				|| (tmp.charAt(4) - tmp.charAt(6) != -44)
				|| ((tmp.charAt(6) ^ tmp.charAt(8)) != 19)
				|| (tmp.charAt(9) - tmp.charAt(5) != 25)
				|| (tmp.charAt(0) + tmp.charAt(5) + tmp.charAt(7) != 291)
				|| ((tmp.charAt(10) ^ tmp.charAt(5)) != 21)
				|| (tmp.charAt(1) != tmp.charAt(13))
				|| (tmp.charAt(11) != 111)
				|| (s.charAt(s.length() - 2) != 63)) {
			ret = false;
		}
		return ret;
	}

	public static void main(String[] args) {
		boolean[] isDigit = { false, false, false, false, false, false, false, false, false, false, true, false,
				false, false, false, true, false, false, false, true, false, false, false, false, false, false, false,
				false, true, false, true, false, false, false, false, false, false, false, false, false, false, false,
				false, false, true, false, false, false, false, true, false, false, false, false, false, false, false };
		int[] pos = { 17, 21, 24, 29, 32, 35, 38, 47, 52 };
		char[] let = { 't', 'P', 'i', 'o', 't', 'L', 'n', 'y', 'i', 'm', 'h', 'r', 'c', 'p', 'o', 'h', 'r', 'i',
				'P', 'm' };
		Scanner inp = new Scanner(System.in);
		System.out.print("Enter flag: ");
		String input = inp.next();
		boolean ret = true;
		if (check(check(check(check(check(ret, input), input, isDigit), input, pos), input, let), input, ""))
			System.out.println("Flag is correct");
		else
			System.out.println("Try another one");
	}
}
