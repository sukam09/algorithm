function solution(commands) {
  const arr = [...Array(50)].map(() => Array(50).fill(''));
  const cell = [...Array(50)].map((_, i) => [...Array(50)].map((_, j) => [i, j]));

  const update1 = (r, c, value) => {
    const cells = cell[r][c];
    for (let i = 0; i < cells.length; i += 2) {
      const rr = cells[i];
      const cc = cells[i + 1];
      arr[rr][cc] = value;
    }
  };

  const update2 = (v1, v2) => {
    for (let i = 0; i < 50; i++) {
      for (let j = 0; j < 50; j++) {
        if (arr[i][j] === v1) {
          arr[i][j] = v2;
        }
      }
    }
  };

  const merge = (r1, c1, r2, c2) => {
    if (cell[r1][c1] === cell[r2][c2]) return;
    let val = arr[r1][c1];
    if (val === '') val = arr[r2][c2];
    let nc = [...cell[r1][c1], ...cell[r2][c2]];
    for (let i = 0; i < nc.length; i += 2) {
      const rr = nc[i];
      const cc = nc[i + 1];
      cell[rr][cc] = nc;
      arr[rr][cc] = val;
    }
  };

  const unmerge = (r, c) => {
    const cells = cell[r][c];
    const val = arr[cells[0]][cells[1]];
    for (let i = 0; i < cells.length; i += 2) {
      const rr = cells[i];
      const cc = cells[i + 1];
      cell[rr][cc] = [rr, cc];
      arr[rr][cc] = '';
    }
    arr[r][c] = val;
  };

  const ans = [];

  for (command of commands) {
    const cmd = command.split(' ');
    const query = cmd[0];
    if (query === 'UPDATE') {
      if (cmd.length === 4) {
        let [_, r, c, value] = cmd;
        r = +r;
        r--;
        c = +c;
        c--;
        update1(r, c, value);
      } else {
        const [_, value1, value2] = cmd;
        update2(value1, value2);
      }
    } else if (query === 'MERGE') {
      let [_, r1, c1, r2, c2] = cmd;
      r1 = +r1;
      r1--;
      c1 = +c1;
      c1--;
      r2 = +r2;
      r2--;
      c2 = +c2;
      c2--;
      merge(r1, c1, r2, c2);
    } else if (query === 'UNMERGE') {
      let [_, r, c] = cmd;
      r = +r;
      r--;
      c = +c;
      c--;
      unmerge(r, c);
    } else {
      let [_, r, c] = cmd;
      r = +r;
      r--;
      c = +c;
      c--;
      let target = arr[r][c];
      if (target === '') target = 'EMPTY';
      ans.push(target);
    }
  }

  return ans;
}