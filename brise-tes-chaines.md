---
layout: standalone
title: "Brisé ? Reprenez le contrôle"
author: "Guillaume"
last_modified_at: 2024-11-06T21:00:52-05:00
---

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title }}</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      background: url('/images/Brise-tes-chaines_edited.jpg') no-repeat center center fixed;
      background-size: cover;
      color: #fff;
    }
    .content-container {
      position: relative;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      background-color: rgba(0, 0, 0, 0.7);
      border-radius: 10px;
    }
    .title-background {
      text-align: center;
      margin-bottom: 20px;
    }
    .title-background h1 {
      font-size: 2.5em;
      font-weight: bold;
      margin: 0 0 10px 0;
    }
    .title-background h2 {
      font-size: 1.5em;
      margin: 0;
      font-weight: normal;
    }
    /* CTA haut de page */
    .cta-top {
      text-align: center;
      margin: 25px 0;
      padding: 20px;
      background-color: rgba(255, 255, 255, 0.9);
      color: #000;
      border-radius: 10px;
    }
    .cta-top h3 {
      margin-top: 0;
      font-size: 1.2em;
    }
    .cta-top button {
      font-size: 1.2em;
      color: #fff;
      background-color: #d9534f;
      border: none;
      border-radius: 5px;
      padding: 10px 20px;
      cursor: pointer;
      margin-top: 10px;
    }
    .cta-top button:hover {
      background-color: #c9302c;
    }

    .benefits-intro {
      margin-top: 20px;
      font-size: 1.1em;
      line-height: 1.4em;
    }

    .benefits-list {
      padding: 15px;
      margin: 20px 0;
      background-color: rgba(200, 240, 200, 0.9);
      border-radius: 10px;
      color: #000;
      font-size: 1.1em;
    }
    .benefits-list li {
      margin-bottom: 10px;
      list-style: none;
    }
    .benefits-list li:before {
      content: "✔";
      color: green;
      margin-right: 10px;
    }

    /* Social Proof / Intro */
    .social-proof {
      background-color: rgba(255, 255, 255, 0.9);
      color: #000;
      margin: 20px 0;
      padding: 20px;
      border-radius: 10px;
      font-size: 1.1em;
      line-height: 1.4em;
    }

    /* Testimonials Block */
    .testimonials {
      margin: 30px 0;
      text-align: center;
    }
    .testimonials h3 {
      margin-bottom: 20px;
    }

    .testimonial-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      grid-template-rows: repeat(2, auto);
      grid-gap: 20px;
      justify-items: center;
      margin: 0 auto;
      max-width: 600px;
    }
    .testimonial-item {
      background-color: rgba(255, 255, 255, 0.9);
      padding: 10px;
      border-radius: 10px;
      color: #000;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      box-sizing: border-box;
      text-align: center;
    }
    .testimonial-item img {
      width: 60px;
      height: 60px;
      border-radius: 50%;
      margin-bottom: 10px;
    }
    .testimonial-item p {
      font-size: 0.95em;
      margin-bottom: 10px;
      line-height: 1.3em;
    }
    .stars {
      color: #f1c40f;
      font-size: 1.2em;
    }

    .cta-box {
      text-align: center;
      margin: 30px 0;
      padding: 20px;
      color: #000;
      background-color: rgba(200, 240, 200, 0.9);
      border-radius: 10px;
    }
    .cta-box button {
      font-size: 1.2em;
      color: #fff;
      background-color: #d9534f;
      border: none;
      border-radius: 5px;
      padding: 10px 20px;
      cursor: pointer;
    }
    .cta-box button:hover {
      background-color: #c9302c;
    }
    iframe {
      display: block;
      margin: 20px auto;
      border-radius: 10px;
    }
    /* Styles for the FAQ section */
    .faq-section {
      margin-top: 40px; /* Space from the form */
      background-color: rgba(255, 255, 255, 0.9);
      color: #000;
      padding: 20px;
      border-radius: 10px;
    }
    .faq-question {
      cursor: pointer;
      margin-bottom: 10px;
      border-bottom: 1px solid #ddd; /* Subtle separator */
      padding-bottom: 5px;
      font-weight: bold;
    }
    .faq-answer {
      display: none; /* Initially hide the answers */
      margin-left: 20px; /* Indentation for answers */
      margin-bottom: 15px;
    }
  </style>
  {% include head-custom.html %}
</head>

<body>
  <div class="content-container">
    <div class="title-background">
      <!-- Nouveau titre plus précis -->
      <h1>Brisé après une trahison ?</h1>
      <h2>Reprenez le contrôle de vos émotions dès aujourd’hui.</h2>
    </div>

    <!-- CTA en haut de page -->
    <div class="cta-top">
      <h3>Accédez à une formation offerte pour tourner la page, retrouver confiance et clarté et reprendre le contrôle de votre vie.</h3>
      <!-- Updated onclick to scroll to a container rather than the script itself -->
      <button onclick="document.getElementById('form-container').scrollIntoView({ behavior: 'smooth' })">
        Obtenir ma formation gratuite
      </button>
    </div>
    <div class="social-proof">
      <p>Si tu lis ces lignes, c'est que tu traverses probablement une période difficile. <br> Rupture, trahison... La douleur est immense, je le sais. </p> <p>C'est pour aider des hommes comme toi que j'ai créé <b>lapres-liaison.com</b></p>
      
      <p><strong>Vous n’êtes pas seul. Vous n’êtes PLUS seul. </strong></p>
      Depuis plus de 2 ans, j’accompagne des d’hommes à surmonter la douleur et à retrouver la maîtrise de leurs émotions. <br>
      <p>Dans cette formation en 3 jours, je vous donne un plan clair et concret pour reconstruire votre confiance et reprendre votre vie en main.</p>
    </div>
    <h3><strong>Voici comment se déroulent les 3 jours de formation:</strong></h3>
    <ul class="benefits-list">
      <li><strong>Jour 1 :</strong> Comment <b>soulager votre douleur instantanément</b> et faire le premier pas vers la résilience.</li>
      <li><strong>Jour 2 :</strong> <b>"Pourquoi moi ?"</b>: Les questions fusent.  Comprenez enfin les raisons profondes de cette épreuve et libérez-vous du poids des "et si...".  </li>
      <li><strong>Jour 3 :</strong> Apprenez à <b>tirer les leçons</b> de cette expérience douloureuse. Découvrez comment identifier vos schémas relationnels et construire un avenir plus sain et plus épanouissant.</li>
    </ul>
    <!-- Petit bloc de social proof supplémentaire -->
    <div class="social-proof">
      <strong>J'ai aidé plus d’une centaine d’hommes</strong> à se relever de situations similaires : 
      <li>perte de confiance,</li>
      <li>angoisses après une trahison,</li>
      <li>peurs de se reconstruire… </li>
      <br><strong>Résultat :</strong> ils ont pu reprendre le contrôle de leurs émotions et franchir cette épreuve avec plus de clarté et de force. Lis leurs témoignages, ils sont inspirants ! 👇
    </div>

    <!-- Testimonials Block -->
    <div class="testimonials">
      <h3>Ce que disent nos participants :</h3>
      <div class="testimonial-grid">
        <div class="testimonial-item">
          <img src="/images/people/Matthieu.png" alt="Photo de client">
          <p>“Avant, j’étais bloqué dans la douleur et le doute. Grâce aux conseils de Guillaume, j’ai pu me relever en quelques semaines. Merci pour ton aide précieuse !”</p>
          <div class="stars">★★★★★</div>
        </div>
        <div class="testimonial-item">
          <img src="/images/people/Louis.png" alt="Photo de client">
          <p>“Je me sens enfin à nouveau moi-même, avec une confiance retrouvée. J’ai appris à gérer mes émotions sans supplier mon ex. Hautement recommandé !”</p>
          <div class="stars">★★★★★</div>
        </div>
        <div class="testimonial-item">
          <img src="/images/people/Nicolas.png" alt="Photo de client">
          <p>“Une méthode puissante et pratique pour se relever rapidement et dignement. J’avais peur de ne jamais tourner la page, mais maintenant je me sens plus fort.”</p>
          <div class="stars">★★★★★</div>
        </div>
        <div class="testimonial-item">
          <img src="/images/people/bill.avif" alt="Photo de client">
          <p>“J’étais complètement abattu. Aujourd’hui, je me sens prêt à avancer. le travail avec Guillaume a vraiment changé ma façon de réagir à la douleur.”</p>
          <div class="stars">★★★★★</div>
        </div>
      </div>
    </div>

    <!-- CTA final -->
    <div class="cta-box">
      <p><strong>Vous aussi, libérez-vous de la souffrance et reconstruisez-vous plus fort que jamais.</strong></p>
      <p><em>Inscrivez-vous gratuitement dès maintenant pour découvrir la méthode PARIS et maîtriser vos émotions.</em></p>

      <p><em style="font-style: italic;">"N'attends pas ; les solutions existent. Ne fais pas de la souffrance ton choix."</em> Coach Guillaume</p>
    </div>

    <!-- Visible container that wraps the form -->
    <div id="form-container" style="margin-top: 40px;">
      <script
        id="sg-script-675f5362b6045"
        data-url="eyJmb3JtIjo3MzYzMCwidXNlciI6IjQ3NDk3In0-"
        src="https://sg-autorepondeur.com/plugins/form/widget.js">
      </script>
    </div>
    
    <div class="faq-section">
      <h3>Foire aux questions</h3>
      <div class="faq-question">➤  À qui s'adresse cette formation ?</div>
      <div class="faq-answer">Cette formation est conçue pour les hommes qui ont vécu une rupture ou une trahison et qui cherchent à surmonter la douleur, à reprendre confiance en eux et à avancer sereinement dans leur vie.</div>

      <div class="faq-question">➤ Qui ne devrait PAS suivre la formation ?</div>
      <div class="faq-answer"> Cette formation n'est pas adaptée si tu es suicidaire, en urgence psychiatrique ou si tu préfères te plaindre et ne rien faire pour changer ta situation. <br> J'accompagne uniquement les personnes motivées et prêtes à s'investir dans leur développement personnel. "Aide toi et le ciel t'aidera."</div>

      <div class="faq-question">➤  Est-ce que cette formation convient à tous les types de ruptures ?</div>
      <div class="faq-answer">Oui, que vous ayez vécu une séparation amoureuse, une infidélité, ou une trahison amicale, la formation vous donnera des outils pour gérer vos émotions et reconstruire votre vie.</div>

      <div class="faq-question">➤ Est-ce que cette formation est vraiment gratuite ?</div>
      <div class="faq-answer">Oui, trop d'hommes souffrent seuls et en silence. La formation vous donne accès à des conseils concrets pour vous aider à vous relever. Elle est suivie d'une invitation à rejoindre ma toute nouvelle initiative: une communauté facebook gratuite de soutien. <br>Ceci est une offre de lancement. Je ne sais pas combien de temps cela durera.</div>

      <div class="faq-question"> ➤ Combien de temps faut-il pour voir les premiers résultats ?</div>
      <div class="faq-answer">Laformule PARIS est extrêmement efficace et a déjà aidé des hommes en situation de blocage complet, parfois depuis des années. Ceci dit, PARIS n'est pas une formule miracle puisqu'elle requiert de la pratiquer régulièrement (particulièrement au début) pour avoir un effet profond et durable. On n'a rien sans rien. Mais l'investissement en vaut la chandelle</div>

      <div class="faq-question">➤ Je ne suis pas sûr d'être prêt à m'engager dans une formation. Que faire ?</div>
      <div class="faq-answer">C'est aussi pourquoi elle n'est que de 3 jours. <br>L'indécision est la pire des situations. Tu peux choisir de continuer à souffrir ou choisir de travailler sur toi. Le choix est tien. Tu n'as rien à perdre et tout à gagner.</div>

      <div class="faq-question">➤ En quoi la méthode PARIS est-elle différente des autres approches ?</div>
      <div class="faq-answer">La méthode PARIS est une séquence unique. Elle rassemble les meilleurs outils, optimisés pour une efficacité maximale. Tu ne trouveras cette synergie nulle part ailleurs.</div>
    </div>
  </div>

  <script>
    // JavaScript to toggle FAQ answers
    const questions = document.querySelectorAll('.faq-question');

    questions.forEach(question => {
      question.addEventListener('click', () => {
        const answer = question.nextElementSibling;
        answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
      });
    });
  </script>
</body>
