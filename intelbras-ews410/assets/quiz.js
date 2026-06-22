/* Shared quiz engine for all lessons.
 *
 * Markup contract (see lesson.css for styling):
 *   <div class="quiz" id="q1">
 *     <div class="q">…question…</div>
 *     <button class="opt" data-correct="1">right answer</button>
 *     <button class="opt">wrong answer</button>
 *     <div class="fb"></div>
 *   </div>
 *   …optional…
 *   <div class="card" id="scorecard" style="display:none">
 *     <strong>Scorecard:</strong> <span id="score"></span>
 *     <p class="note" id="scorenote"></p>
 *   </div>
 *
 * Usage at the end of a lesson:
 *   const FEEDBACK = { q1: 'explanation html…', q2: '…' };
 *   initQuiz(FEEDBACK);
 *
 * Each FEEDBACK[id] is the explanation shown after answering that quiz, prefixed
 * automatically with a Correct/Not-quite marker. Scorecard updates once all
 * quizzes on the page are answered (it's optional — omit the element to skip).
 */
function initQuiz(FEEDBACK, opts) {
  opts = opts || {};
  const quizzes = document.querySelectorAll('.quiz');
  const total = quizzes.length;
  let answered = 0, correct = 0;

  quizzes.forEach(quiz => {
    const opts2 = quiz.querySelectorAll('.opt');
    const fb = quiz.querySelector('.fb');
    opts2.forEach(opt => opt.addEventListener('click', () => {
      if (quiz.dataset.done) return;
      quiz.dataset.done = '1';
      answered++;
      const right = opt.dataset.correct === '1';
      if (right) correct++;
      opts2.forEach(o => {
        o.disabled = true;
        if (o.dataset.correct === '1') o.classList.add('correct');
      });
      if (!right) opt.classList.add('wrong');
      fb.classList.add('show');
      fb.innerHTML = (right
        ? '<strong style="color:var(--good)">Correct.</strong> '
        : '<strong style="color:var(--bad)">Not quite.</strong> ')
        + (FEEDBACK[quiz.id] || '');
      if (answered === total) showScore(correct, total, opts.perfect, opts.partial);
    }));
  });
}

function showScore(correct, total, perfectMsg, partialMsg) {
  const sc = document.getElementById('scorecard');
  if (!sc) return;
  sc.style.display = 'block';
  const s = document.getElementById('score');
  if (s) s.textContent = correct + ' / ' + total;
  const n = document.getElementById('scorenote');
  if (n) n.textContent = correct === total
    ? (perfectMsg || 'Clean sweep — that skill is yours. Now run it on your own machine.')
    : (partialMsg || 'Re-read the procedure for any you missed, then try the real-world task below.');
  sc.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/* Shared light/dark cycle, used by the .theme-toggle button on every page. */
function cycleTheme() {
  const h = document.documentElement;
  const c = h.getAttribute('data-theme');
  h.setAttribute('data-theme', c === 'dark' ? 'light' : c === 'light' ? '' : 'dark');
}
