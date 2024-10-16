function solution(numbers) {
  const binary = n => {
    let s = '';
    while (n > 0) {
      const r = (n % 2) + '';
      s = r + s;
      n = Math.floor(n / 2);
    }
    return s;
  };

  const find = n => {
    let pow = 2;

    while (1) {
      if (pow - 1 >= n) {
        return pow - 1;
      }
      pow *= 2;
    }
  };

  const ans = [];
  let tree = '';
  let possible = 1;

  const dfs = (st, en) => {
    if (st === en) {
      // leaf
      return;
    }

    const r = (st + en) / 2;
    // lc: st ~ r - 1
    // rc: r + 1 ~ en

    const lcr = (st + r - 1) / 2;
    const rcr = (r + 1 + en) / 2;

    if (tree[r] === '0' && (tree[lcr] === '1' || tree[rcr] === '1')) {
      possible = 0;
      return;
    }

    dfs(st, r - 1);
    dfs(r + 1, en);
  };

  const solve = num => {
    let bin = binary(num);
    const len = bin.length;
    const tg = find(len);

    let remain = tg - len;
    while (remain--) {
      bin = '0' + bin;
    }

    tree = bin;
    possible = 1;

    dfs(0, bin.length - 1);
  };

  for (const num of numbers) {
    solve(num);
    ans.push(possible);
  }

  return ans;
}
