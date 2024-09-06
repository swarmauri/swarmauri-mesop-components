import {
  LitElement,
  html,
  css
} from 'https://cdn.jsdelivr.net/gh/lit/dist@3/core/lit-core.min.js';

class CounterComponent extends LitElement {
  static properties = {
    answer: {type: Boolean},
    toggleEvent: {type: String},
  };
  
  static styles = css`
    .container {
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #efefef;
    }

    .card {
      height: 400px;
      width: 250px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #fff;
      border-radius: 20px;
      box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
      cursor: pointer;
      position: relative;
      transition: transform 0.8s;
      transform-style: preserve-3d;
    }

    .card p {
      font-size: 16px;
      font-weight: 400;
      font-family: sans-serif;
    }

    .card.flipped {
      transform: rotateY(180deg);
    }

    .front, .back {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
	  border-radius: 20px;
    }

    .back {
      transform: rotateY(180deg);
      background-color: #2980b9;
      color: white;
    }
  `;

  constructor() {
    super();
    this.answer = false;
    this.toggleEvent = '';
  }

  render() {
    return html`
      <div class="container">
        <div class="card ${this.answer ? 'flipped' : ''}" @click="${this._onToggle}">
          <div class="front">
            <p>QUESTION</p>
          </div>
          <div class="back">
            <p>ANSWER</p>
          </div>
        </div>
      </div>
    `;
  }

  _onToggle() {
    this.dispatchEvent(
      new MesopEvent(this.toggleEvent, {
        answer: !this.answer,
      }),
    );
  }
}

customElements.define('flipcard-component', CounterComponent);
