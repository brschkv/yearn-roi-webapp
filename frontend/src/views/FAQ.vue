<template>
  <div class="about">
    <div>
      <h4>What am I looking at?</h4>
      <p>This is a try to model the future developments of the PricePerShare value of yearn vaults
        by doing a bayesian estimation based on past price developments. For a more detailed description
        please refer to <a href="https://github.com/brschkv/yearn-roi-model/blob/master/DISCUSSION.md"> this
          discussion</a>.
        The model estimates prices of the next n days ("Horizon") based on the prices of the last m ("Based on last") days.
        The short of it is this: According to the model(!!) there is a 50% chance that the future price at
        a given date is within the blue area (This is called the 'Highest Posterior Density' or 'HPD' in bayesian terms).
        And, according to the model(!!), there is a 95% chance that the future price is within the grey area.
      </p>
      <div>
        <h4>Is this financial advice?</h4>
        <p>This is most certainly NOT financial advice. You should do your own research. If this tool
          helps you doing it, all the better.
        </p>
      </div>
      <div>
        <h4>Is the code open source?</h4>
        <p>Yes, there is a github repo for
          <a href="https://github.com/brschkv/yearn-roi-model">the model</a> and for
          <a href="https://github.com/brschkv/yearn-roi-webapp">the webapp</a>.
        </p>
      </div>
      <div>
        <h4>I have some cool ideas how to improve this. Are you open to that?</h4>
        <p>I strongly believe that good models and good apps are built by constantly
          discussing them. If you have ideas to make any of these better,
          or just a question, open up a github issue or drop me a mail at yearn-roi@protonmail.com
        </p>
      </div>
      <div>
        <h4>Why is this page so ugly?</h4>
        <p>I really hate Frontend Development. Because I am really bad at Frontend Development.
          Because I really hate Frontend Development... It's a vicious cycle.
        </p>
      </div>
    </div>
  </div>
</template>
