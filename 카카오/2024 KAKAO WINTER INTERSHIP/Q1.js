function solution(friends, gifts) {
  const n = friends.length;
  const giftJisu = Array(n).fill(0);
  const arr = [...Array(n)].map(() => Array(n).fill(0));
  const map = new Map();
  const g = Array(n).fill(0);

  let unused = 0;

  for (const gift of gifts) {
    const [a, b] = gift.split(' ');

    // a가 b에게 선물을 줌
    let ai, bi;

    if (map.has(a)) {
      ai = map.get(a);
    } else {
      map.set(a, unused++);
      ai = map.get(a);
    }
    if (map.has(b)) {
      bi = map.get(b);
    } else {
      map.set(b, unused++);
      bi = map.get(b);
    }

    arr[ai][bi]++;
    giftJisu[ai]++;
    giftJisu[bi]--;
  }

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      // 현재 i를 보고 있음
      if (arr[i][j] > arr[j][i]) {
        g[i]++;
      } else if (arr[i][j] < arr[j][i]) {
        g[j]++;
      } else if (giftJisu[i] > giftJisu[j]) {
        g[i]++;
      } else if (giftJisu[i] < giftJisu[j]) {
        g[j]++;
      }
    }
  }

  return Math.max(...g);
}