function solution(users, emoticons) {
  const rates = [0.1, 0.2, 0.3, 0.4];
  const cands = [];
  const m = emoticons.length;
  const arr = Array(m).fill(0);

  const dfs = k => {
    if (k === m) {
      cands.push([...arr]);
      return;
    }
    for (let i = 0; i < 4; i++) {
      arr[k] = i;
      dfs(k + 1);
    }
  };

  dfs(0);

  const ret = [];

  for (const cand of cands) {
    let emoplus = 0;
    let emomoney = 0;
    for (const [rate, cost] of users) {
      let money = 0;
      for (let i = 0; i < m; i++) {
        if (rates[cand[i]] < rate / 100) {
          continue;
        }
        money += emoticons[i] * (1 - rates[cand[i]]);
      }
      if (money >= cost) {
        emoplus++;
      } else {
        emomoney += money;
      }
    }

    ret.push([emoplus, emomoney]);
  }

  ret.sort((a, b) => {
    if (a[0] === b[0]) {
      return b[1] - a[1];
    }
    return b[0] - a[0];
  });

  return ret[0];
}
