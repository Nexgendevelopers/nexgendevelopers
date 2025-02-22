let date = new Date();
let year = date.getFullYear();
document.getElementById("year").innerHTML = year;


// footer
class Footer extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
        <div class="section">
        <div class="container-fluid">
          <div class="footer">
            <div class="sort-note">
              <a class="navbar-brand" href="index.html">NexGen Developers</a>
              <p>We are NexGen Developers, experts in web development, app development, AI, ML models, chatbots, SEO, and more.</p>
              <hr style="margin: 20px 0; color: rgb(82, 82, 82); width: 60%;">
              
            </div>
            
            
          </div>
        </div>
      </div>
    </footer>`;
  }
}

customElements.define("main-footer", Footer);

// Back to top
const amountScrolled = 200;
const btnBackToTop = document.querySelector('.back-to-top');

const backToTop = () => window.scrollTo({ top: 0, behavior: 'smooth' });
const toggleBtnBackToTop = () => {
  window.scrollY > amountScrolled 
    ? btnBackToTop.classList.add('back-to-top_show')
    : btnBackToTop.classList.remove('back-to-top_show');
}

btnBackToTop.addEventListener('click', backToTop);
window.addEventListener('scroll', toggleBtnBackToTop);
