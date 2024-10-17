function solution(dice) {
  const n = dice.length;
  const cand = Array(n / 2).fill(-1); // A
  const vis = Array(n).fill(0);
  let ans = [];
  let mx = 0;
  let b = [];
  let awin = 0;

  const sim = arr => {
    // arr은 현재 시뮬레이션을 돌리는 주사위 셋의 인덱스 리스트
    const map = new Map();
    for (const c of cand2) {
      // c: 주사위 셋 안에 있는 주사위 중 몇 번째 주사위들을 사용할 것인지 나타낸 리스트
      // 각각의 c마다 합계가 존재함
      let sum = 0;
      for (let i = 0; i < n / 2; i++) {
        sum += dice[arr[i]][c[i]];
      }
      if (map.has(sum)) {
        map.set(sum, map.get(sum) + 1);
      } else {
        map.set(sum, 1);
      }
    }
    return map;
  };

  const roll = () => {
    const amap = sim(cand);
    const bmap = sim(b);
    let ret = 0;
    for (const [ak, av] of amap) {
      for (const [bk, bv] of bmap) {
        if (ak > bk) {
          ret += av * bv;
        }
      }
    }
    return ret;
  };

  const solve = () => {
    b = [];
    awin = 0;
    for (let i = 0; i < n; i++) {
      if (!cand.includes(i)) {
        b.push(i);
      }
    }
    const ret = roll();
    if (ret > mx) {
      mx = ret;
      ans = [...cand];
    }
  };

  const dfs = k => {
    if (k === n / 2) {
      solve();
      return;
    }
    let st = 0;
    if (k > 0) {
      st = cand[k - 1] + 1;
    }
    for (let i = st; i < n; i++) {
      if (vis[i]) {
        continue;
      }
      vis[i] = 1;
      cand[k] = i;
      dfs(k + 1);
      vis[i] = 0;
    }
  };

  const cand2 = [];
  const arr = Array(n / 2).fill(-1);

  const dfs2 = k => {
    if (k === n / 2) {
      cand2.push([...arr]);
      return;
    }
    for (let i = 0; i < 6; i++) {
      arr[k] = i;
      dfs2(k + 1);
    }
  };

  dfs2(0);
  dfs(0);

  ans = ans.map(v => v + 1);
  return ans;
}