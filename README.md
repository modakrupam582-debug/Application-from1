index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DOEACC O Level Application Form</title>
  <style>
    :root {
      --bg-1: #07111f;
      --bg-2: #172554;
      --bg-3: #312e81;
      --glass: rgba(255,255,255,0.13);
      --glass-border: rgba(255,255,255,0.18);
      --text-dark: #172033;
      --muted: #475569;
      --primary: #6366f1;
      --secondary: #06b6d4;
      --accent: #ec4899;
      --success: #16a34a;
      --danger: #ef4444;
      --card-bg: rgba(255,255,255,0.93);
      --shadow: 0 30px 70px rgba(0,0,0,.35), 0 8px 20px rgba(0,0,0,.18), inset 0 1px 0 rgba(255,255,255,.9);
    }

    * { box-sizing: border-box; }

    html {
      scroll-behavior: smooth;
    }

    body {
      margin: 0;
      font-family: "Segoe UI", Arial, sans-serif;
      color: var(--text-dark);
      min-height: 100vh;
      overflow-x: hidden;
      background:
        radial-gradient(circle at 12% 15%, rgba(99,102,241,.36), transparent 26%),
        radial-gradient(circle at 88% 18%, rgba(6,182,212,.28), transparent 24%),
        radial-gradient(circle at 50% 100%, rgba(236,72,153,.24), transparent 30%),
        linear-gradient(135deg, var(--bg-1), var(--bg-2) 48%, var(--bg-3));
      background-attachment: fixed;
    }

    .scene {
      position: fixed;
      inset: 0;
      overflow: hidden;
      pointer-events: none;
      perspective: 1600px;
      z-index: 0;
    }

    .orb {
      position: absolute;
      border-radius: 50%;
      filter: blur(14px);
      opacity: .7;
      animation: floatOrb linear infinite;
      transform-style: preserve-3d;
    }

    .orb.one {
      width: 230px;
      height: 230px;
      left: 8%;
      top: 12%;
      background: radial-gradient(circle at 30% 30%, rgba(255,255,255,.75), rgba(99,102,241,.25), transparent 70%);
      animation-duration: 18s;
    }

    .orb.two {
      width: 280px;
      height: 280px;
      right: 8%;
      top: 18%;
      background: radial-gradient(circle at 30% 30%, rgba(255,255,255,.65), rgba(6,182,212,.26), transparent 68%);
      animation-duration: 22s;
    }

    .orb.three {
      width: 300px;
      height: 300px;
      left: 40%;
      bottom: -60px;
      background: radial-gradient(circle at 30% 30%, rgba(255,255,255,.55), rgba(236,72,153,.20), transparent 70%);
      animation-duration: 20s;
    }

    .grid-floor {
      position: absolute;
      left: -10%;
      right: -10%;
      bottom: -30vh;
      height: 55vh;
      transform: rotateX(80deg);
      transform-origin: center top;
      background-image:
        linear-gradient(rgba(255,255,255,.16) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.16) 1px, transparent 1px);
      background-size: 48px 48px;
      mask-image: linear-gradient(to bottom, rgba(255,255,255,.95), rgba(255,255,255,0));
      opacity: .28;
      animation: gridMove 8s linear infinite;
    }

    body::before {
      content: "";
      position: fixed;
      inset: 0;
      background: linear-gradient(120deg, rgba(255,255,255,.06), transparent 40%, rgba(255,255,255,.04));
      pointer-events: none;
      z-index: 0;
    }

    .page {
      position: relative;
      z-index: 2;
      padding: 42px 18px 72px;
    }

    .hero {
      max-width: 1180px;
      margin: 0 auto 24px;
      text-align: center;
      transform-style: preserve-3d;
    }

    .badge {
      display: inline-block;
      padding: 9px 18px;
      margin-bottom: 16px;
      border: 1px solid rgba(255,255,255,.2);
      border-radius: 999px;
      background: rgba(255,255,255,.09);
      color: #fff;
      letter-spacing: 1.8px;
      font-size: 12px;
      font-weight: 700;
      box-shadow: 0 10px 24px rgba(0,0,0,.18);
      backdrop-filter: blur(10px);
    }

    h1 {
      margin: 0;
      color: #fff;
      font-size: clamp(30px, 5vw, 54px);
      font-weight: 800;
      letter-spacing: 2px;
      text-shadow: 0 14px 34px rgba(0,0,0,.34);
      transform: translateZ(24px);
    }

    .subtitle {
      max-width: 860px;
      margin: 14px auto 0;
      color: rgba(255,255,255,.85);
      line-height: 1.65;
      font-size: 16px;
    }

    .shell {
      max-width: 1180px;
      margin: 0 auto;
      perspective: 1800px;
    }

    .form-panel {
      position: relative;
      padding: 28px;
      border-radius: 28px;
      background: linear-gradient(145deg, rgba(255,255,255,.95), rgba(245,248,255,.92));
      box-shadow: var(--shadow);
      border: 1px solid rgba(255,255,255,.75);
      backdrop-filter: blur(18px);
      transform-style: preserve-3d;
      transition: transform .2s ease-out, box-shadow .2s ease-out;
      overflow: hidden;
    }

    .form-panel::before {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, rgba(99,102,241,.08), transparent 34%, rgba(6,182,212,.08), transparent 65%, rgba(236,72,153,.08));
      pointer-events: none;
    }

    .status {
      position: relative;
      z-index: 2;
      margin-bottom: 18px;
      padding: 14px 18px;
      border-radius: 16px;
      font-weight: 600;
      box-shadow: 0 10px 24px rgba(15,23,42,.08);
    }

    .status.success {
      color: #14532d;
      background: linear-gradient(135deg, rgba(34,197,94,.16), rgba(16,185,129,.10));
      border: 1px solid rgba(34,197,94,.25);
    }

    .status.error {
      color: #7f1d1d;
      background: linear-gradient(135deg, rgba(239,68,68,.14), rgba(244,63,94,.1));
      border: 1px solid rgba(239,68,68,.22);
      margin-bottom: 10px;
    }

    form {
      position: relative;
      z-index: 2;
    }

    fieldset {
      border: 0;
      border-radius: 22px;
      padding: 22px;
      margin: 0 0 20px;
      background: linear-gradient(145deg, #ffffff, #eef4ff);
      box-shadow: 12px 12px 26px rgba(25,45,90,.12), -5px -5px 15px rgba(255,255,255,.85), inset 0 0 0 1px rgba(99,102,241,.12);
      transform-style: preserve-3d;
      transition: transform .3s ease, box-shadow .3s ease;
      opacity: 0;
      transform: translateY(28px) rotateX(8deg);
      animation: cardIn .8s ease forwards;
    }

    fieldset:nth-of-type(1) { animation-delay: .05s; }
    fieldset:nth-of-type(2) { animation-delay: .12s; }
    fieldset:nth-of-type(3) { animation-delay: .18s; }
    fieldset:nth-of-type(4) { animation-delay: .24s; }

    fieldset:hover {
      transform: translateY(-4px) rotateX(1.5deg) translateZ(16px);
      box-shadow: 16px 18px 32px rgba(25,45,90,.16), -5px -5px 16px rgba(255,255,255,.92), inset 0 0 0 1px rgba(99,102,241,.18);
    }

    legend {
      padding: 10px 18px;
      border-radius: 999px;
      color: #fff;
      font-weight: 800;
      letter-spacing: .5px;
      background: linear-gradient(135deg, #4f46e5, #06b6d4, #ec4899);
      box-shadow: 0 8px 18px rgba(79,70,229,.28);
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 18px 22px;
      margin-top: 12px;
    }

    .field {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .field.full {
      grid-column: 1 / -1;
    }

    label {
      font-weight: 700;
      color: #334155;
      font-size: 14px;
    }

    .inline {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      align-items: center;
      padding-top: 8px;
    }

    .inline label.choice {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-weight: 600;
      color: var(--muted);
    }

    input[type=text],
    input[type=email],
    input[type=tel],
    input[type=date],
    select,
    input[type=file] {
      width: 100%;
      padding: 12px 14px;
      border-radius: 12px;
      border: 1px solid #c7d2fe;
      background: rgba(255,255,255,.97);
      color: var(--text-dark);
      outline: none;
      box-shadow: inset 2px 2px 5px rgba(30,41,59,.07), 0 3px 8px rgba(30,41,59,.05);
      transition: border-color .2s ease, box-shadow .2s ease, transform .2s ease;
    }

    input:focus,
    select:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 4px rgba(99,102,241,.13), 0 8px 18px rgba(79,70,229,.14);
      transform: translateY(-1px);
    }

    input[type=file] {
      border-style: dashed;
      background: #f5f7ff;
      padding: 10px;
    }

    input[type=radio],
    input[type=checkbox] {
      accent-color: var(--primary);
      transform: scale(1.12);
    }

    .language-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      overflow: hidden;
      border-radius: 16px;
      box-shadow: 0 8px 18px rgba(30,41,59,.08);
      margin-top: 14px;
    }

    .language-table th,
    .language-table td {
      border: 1px solid #dbeafe;
      padding: 14px 12px;
      text-align: center;
    }

    .language-table th {
      color: #fff;
      background: linear-gradient(135deg, #4f46e5, #0891b2);
    }

    .language-table tr:nth-child(even) td { background: #f8faff; }
    .language-table tr:hover td { background: #eef2ff; }

    .actions {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 14px;
      margin-top: 26px;
    }

    .btn {
      position: relative;
      min-width: 170px;
      padding: 14px 26px;
      border: 0;
      border-radius: 14px;
      color: #fff;
      font-size: 15px;
      font-weight: 800;
      letter-spacing: .4px;
      cursor: pointer;
      box-shadow: 0 10px 22px rgba(15,23,42,.22);
      transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
      overflow: hidden;
    }

    .btn::before {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(120deg, transparent, rgba(255,255,255,.28), transparent);
      transform: translateX(-100%);
      transition: transform .6s ease;
    }

    .btn:hover::before {
      transform: translateX(100%);
    }

    .btn:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 16px 28px rgba(15,23,42,.28);
      filter: saturate(1.05);
    }

    .btn:active {
      transform: translateY(1px) scale(.98);
    }

    .btn-primary {
      background: linear-gradient(135deg, #16a34a, #06b6d4, #2563eb);
    }

    .btn-secondary {
      background: linear-gradient(135deg, #ef4444, #ec4899, #9333ea);
    }

    .footer-note {
      margin-top: 22px;
      text-align: center;
      color: #64748b;
      font-size: 13px;
    }

    @keyframes floatOrb {
      0% { transform: translate3d(0, 0, 0) scale(1); }
      25% { transform: translate3d(18px, -20px, 80px) scale(1.06); }
      50% { transform: translate3d(-12px, -38px, 140px) scale(.95); }
      75% { transform: translate3d(16px, -10px, 60px) scale(1.03); }
      100% { transform: translate3d(0, 0, 0) scale(1); }
    }

    @keyframes gridMove {
      from { background-position: 0 0, 0 0; }
      to { background-position: 0 48px, 48px 48px; }
    }

    @keyframes cardIn {
      to {
        opacity: 1;
        transform: translateY(0) rotateX(0deg);
      }
    }

    @media (max-width: 860px) {
      .page { padding: 26px 12px 50px; }
      .form-panel { padding: 18px; border-radius: 22px; }
      .grid { grid-template-columns: 1fr; gap: 16px; }
      .language-table th, .language-table td { padding: 10px 8px; }
      .actions { flex-direction: column; }
      .btn { width: 100%; }
    }
  </style>
</head>
<body>
  <div class="scene" aria-hidden="true">
    <div class="orb one"></div>
    <div class="orb two"></div>
    <div class="orb three"></div>
    <div class="grid-floor"></div>
  </div>

  <div class="page">
    <section class="hero">
      <div class="badge">3D GLASSMORPHIC APPLICATION UI</div>
      <h1>DOEACC (O Level) Application Form</h1>
      <p class="subtitle">Complete Flask + HTML/CSS/JavaScript implementation with a 3D animated layout, interactive tilt effect, floating background orbs, form validation, and file upload support.</p>
    </section>

    <div class="shell">
      <div class="form-panel" id="tilt-card">
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}
            {% for category, message in messages %}
              <div class="status {{ 'error' if category == 'error' else 'success' }}">{{ message }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}

        {% if success %}
          <div class="status success">
            Application submitted successfully for <strong>{{ applicant_name }}</strong>. Reference ID: <strong>{{ application_id }}</strong>
            {% if saved_files.photo or saved_files.signature %}
              <div style="margin-top:8px; font-weight:600;">
                {% if saved_files.photo %}Saved photo: {{ saved_files.photo }}{% endif %}
                {% if saved_files.photo and saved_files.signature %}<br>{% endif %}
                {% if saved_files.signature %}Saved signature: {{ saved_files.signature }}{% endif %}
              </div>
            {% endif %}
          </div>
        {% endif %}

        <form action="/" method="post" enctype="multipart/form-data" novalidate>
          <fieldset>
            <legend>Personal Details</legend>
            <div class="grid">
              <div class="field">
                <label for="title">Title</label>
                <select id="title" name="title" required>
                  <option value="">--Select--</option>
                  {% for item in title_options %}
                    <option value="{{ item }}" {% if form.get('title') == item %}selected{% endif %}>{{ item }}</option>
                  {% endfor %}
                </select>
              </div>

              <div class="field">
                <label for="full_name">Applicant's Full Name</label>
                <input id="full_name" name="full_name" type="text" placeholder="Full Name" value="{{ form.get('full_name', '') }}" required>
              </div>

              <div class="field">
                <label>Care Of</label>
                <div class="inline">
                  <label class="choice"><input type="radio" name="care" value="Parents" {% if form.get('care', 'Parents') == 'Parents' %}checked{% endif %}> Parents</label>
                  <label class="choice"><input type="radio" name="care" value="Guardian" {% if form.get('care') == 'Guardian' %}checked{% endif %}> Guardian</label>
                </div>
              </div>

              <div class="field"></div>

              <div class="field">
                <label for="father_name">Father's Name</label>
                <input id="father_name" name="father_name" type="text" placeholder="Father's Name" value="{{ form.get('father_name', '') }}" required>
              </div>

              <div class="field">
                <label for="mother_name">Mother's Name</label>
                <input id="mother_name" name="mother_name" type="text" placeholder="Mother's Name" value="{{ form.get('mother_name', '') }}" required>
              </div>

              <div class="field">
                <label>Gender</label>
                <div class="inline">
                  {% for value in ['Male', 'Female', 'Others'] %}
                    <label class="choice"><input type="radio" name="gender" value="{{ value }}" {% if form.get('gender') == value %}checked{% endif %}> {{ value }}</label>
                  {% endfor %}
                </div>
              </div>

              <div class="field">
                <label for="dob">Date of Birth</label>
                <input id="dob" name="dob" type="date" value="{{ form.get('dob', '') }}" required>
              </div>

              <div class="field">
                <label for="marital_status">Marital Status</label>
                <select id="marital_status" name="marital_status" required>
                  <option value="">--Select--</option>
                  {% for item in marital_status_options %}
                    <option value="{{ item }}" {% if form.get('marital_status') == item %}selected{% endif %}>{{ item }}</option>
                  {% endfor %}
                </select>
              </div>

              <div class="field">
                <label for="category">Category</label>
                <select id="category" name="category" required>
                  <option value="">--Select--</option>
                  {% for item in category_options %}
                    <option value="{{ item }}" {% if form.get('category') == item %}selected{% endif %}>{{ item }}</option>
                  {% endfor %}
                </select>
              </div>

              <div class="field">
                <label>Handicapped</label>
                <div class="inline">
                  {% for value in ['No', 'Yes'] %}
                    <label class="choice"><input type="radio" name="handicapped" value="{{ value }}" {% if form.get('handicapped', 'No') == value %}checked{% endif %}> {{ value }}</label>
                  {% endfor %}
                </div>
              </div>

              <div class="field">
                <label>Ex-Serviceman</label>
                <div class="inline">
                  {% for value in ['No', 'Yes'] %}
                    <label class="choice"><input type="radio" name="serviceman" value="{{ value }}" {% if form.get('serviceman', 'No') == value %}checked{% endif %}> {{ value }}</label>
                  {% endfor %}
                </div>
              </div>

              <div class="field">
                <label>EWS</label>
                <div class="inline">
                  {% for value in ['No', 'Yes'] %}
                    <label class="choice"><input type="radio" name="ews" value="{{ value }}" {% if form.get('ews', 'No') == value %}checked{% endif %}> {{ value }}</label>
                  {% endfor %}
                </div>
              </div>

              <div class="field">
                <label for="religion">Religion</label>
                <select id="religion" name="religion" required>
                  <option value="">--Select--</option>
                  {% for item in religion_options %}
                    <option value="{{ item }}" {% if form.get('religion') == item %}selected{% endif %}>{{ item }}</option>
                  {% endfor %}
                </select>
              </div>
            </div>
          </fieldset>

          <fieldset>
            <legend>Contact Details</legend>
            <div class="grid">
              <div class="field">
                <label for="mobile">Mobile Number</label>
                <input id="mobile" name="mobile" type="tel" pattern="[0-9]{10}" maxlength="10" placeholder="10-digit mobile" value="{{ form.get('mobile', '') }}" required>
              </div>

              <div class="field">
                <label for="email">Email ID</label>
                <input id="email" name="email" type="email" placeholder="you@example.com" value="{{ form.get('email', '') }}" required>
              </div>

              <div class="field">
                <label for="address1">Address Line 1</label>
                <input id="address1" name="address1" type="text" placeholder="House No., Street" value="{{ form.get('address1', '') }}" required>
              </div>

              <div class="field">
                <label for="address2">Address Line 2</label>
                <input id="address2" name="address2" type="text" placeholder="Locality, Landmark" value="{{ form.get('address2', '') }}">
              </div>

              <div class="field">
                <label for="city">City</label>
                <input id="city" name="city" type="text" placeholder="City" value="{{ form.get('city', '') }}" required>
              </div>

              <div class="field">
                <label for="state">State</label>
                <select id="state" name="state" required>
                  <option value="">--Select--</option>
                  {% for item in state_options %}
                    <option value="{{ item }}" {% if form.get('state') == item %}selected{% endif %}>{{ item }}</option>
                  {% endfor %}
                </select>
              </div>

              <div class="field">
                <label for="pincode">Pin Code</label>
                <input id="pincode" name="pincode" type="text" maxlength="6" pattern="[0-9]{6}" placeholder="6-digit PIN" value="{{ form.get('pincode', '') }}" required>
              </div>
            </div>
          </fieldset>

          <fieldset>
            <legend>Language Knowledge</legend>
            <table class="language-table">
              <thead>
                <tr>
                  <th>Language</th>
                  <th>Reading</th>
                  <th>Writing</th>
                  <th>Spoken</th>
                </tr>
              </thead>
              <tbody>
                {% for language in languages %}
                  {% set key = language.lower() %}
                  <tr>
                    <td>{{ language }}</td>
                    <td><input type="checkbox" name="lang_{{ key }}_r" {% if form.get('lang_' ~ key ~ '_r') %}checked{% endif %}></td>
                    <td><input type="checkbox" name="lang_{{ key }}_w" {% if form.get('lang_' ~ key ~ '_w') %}checked{% endif %}></td>
                    <td><input type="checkbox" name="lang_{{ key }}_s" {% if form.get('lang_' ~ key ~ '_s') %}checked{% endif %}></td>
                  </tr>
                {% endfor %}
              </tbody>
            </table>
          </fieldset>

          <fieldset>
            <legend>Identification Details</legend>
            <div class="grid">
              <div class="field">
                <label for="aadhaar">Aadhaar Card Number</label>
                <input id="aadhaar" name="aadhaar" type="text" maxlength="12" pattern="[0-9]{12}" placeholder="12-digit Aadhaar" value="{{ form.get('aadhaar', '') }}">
              </div>

              <div class="field">
                <label for="pan">PAN Card Number</label>
                <input id="pan" name="pan" type="text" maxlength="10" placeholder="ABCDE1234F" value="{{ form.get('pan', '')|upper }}">
              </div>

              <div class="field">
                <label for="photo">Upload Photo</label>
                <input id="photo" name="photo" type="file" accept="image/*">
              </div>

              <div class="field">
                <label for="signature">Upload Signature</label>
                <input id="signature" name="signature" type="file" accept="image/*">
              </div>
            </div>
          </fieldset>

          <div class="actions">
            <button class="btn btn-primary" type="submit">Submit Application</button>
            <button class="btn btn-secondary" type="reset">Reset Form</button>
          </div>

          <div class="footer-note">Built with Flask backend validation and immersive 3D animated UI behavior.</div>
        </form>
      </div>
    </div>
  </div>

  <script>
    const tiltCard = document.getElementById('tilt-card');

    if (tiltCard) {
      const applyTilt = (event) => {
        const rect = tiltCard.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotateY = ((x - centerX) / centerX) * 6;
        const rotateX = -((y - centerY) / centerY) * 4;
        tiltCard.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(10px)`;
        tiltCard.style.boxShadow = `${-rotateY * 2}px ${18 + Math.abs(rotateX * 2)}px 60px rgba(0,0,0,.28), 0 8px 22px rgba(0,0,0,.14), inset 0 1px 0 rgba(255,255,255,.85)`;
      };

      const resetTilt = () => {
        tiltCard.style.transform = 'rotateX(0deg) rotateY(0deg) translateZ(0)';
        tiltCard.style.boxShadow = '0 30px 70px rgba(0,0,0,.35), 0 8px 20px rgba(0,0,0,.18), inset 0 1px 0 rgba(255,255,255,.9)';
      };

      tiltCard.addEventListener('mousemove', applyTilt);
      tiltCard.addEventListener('mouseleave', resetTilt);
      tiltCard.addEventListener('touchend', resetTilt);
    }

    document.querySelectorAll('fieldset').forEach((card, index) => {
      card.addEventListener('mousemove', (event) => {
        const rect = card.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        const rotateY = ((x / rect.width) - 0.5) * 5;
        const rotateX = (0.5 - (y / rect.height)) * 4;
        card.style.transform = `translateY(-4px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(${10 + index * 2}px)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0) rotateX(0deg) rotateY(0deg)';
      });
    });
  </script>
</body>
</html>
