<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4">
      Vault: <b-form-select v-model="vault" :options="vaults"></b-form-select>
      </div>
      <div class="col-md-4">
        Based on last: <b-form-select v-model="base" :options="bases"></b-form-select>
      </div>
       <div class="col-md-4">
         Horizon: <b-form-select v-model="horizon" :options="horizons"></b-form-select>
      </div>
    </div>
    <div class="row mt-3 mb-3">
      <div class="col-md-5">
      </div>
      <div class="col-md-2">
        <div>
          <button type="button" class="align-content-center btn-primary btn" v-on:click="update">Update Chart</button>
        </div>
      </div>
      <div class="col-md-5">
      </div>
    </div>
    <b-row>
      <b-col md="12">
        <line-chart
          v-if="loaded"
          :chartdata="chartdata"
          :options="chartOptions"
        />
      </b-col>
    </b-row>
  </div>
</template>

<script>
import LineChart from './Chart.vue'
import axios from 'axios'

export default {
  name: 'LineChartContainer',
  components: { LineChart },
  methods: {
    update: async function () {
      this.loaded = false
      try {
        const response = await axios.get(`${process.env.VUE_APP_API_PROTOCOL}://${process.env.VUE_APP_API_ADDRESS}:${process.env.VUE_APP_API_PORT}/api/projection/${this.vault}/${this.base}/${this.horizon}`)
        this.chartdata =
          {
            datasets: [
              {
                data: response.data.price,
                fill: false,
                backgroundColor: 'rgba(28, 53, 125,  0.5)',
                borderColor: 'rgba(28, 53, 125, 1)',
                label: ' Historic Price'

              },
              {
                data: response.data.hpd_95_lower,
                fill: false,
                label: '95% HPD',
                backgroundColor: 'rgba(233, 235, 103,0.5)',
                borderColor: 'rgba(233, 235, 103, 0.5)'
              },
              {
                data: response.data.hpd_95_upper,
                fill: +1,
                label: 'hide',
                backgroundColor: 'rgba(233, 235, 103,0.5)',
                borderColor: 'rgba(233, 235, 103, 0.5)'
              },
              {
                data: response.data.hpd_50_lower,
                fill: false,
                label: '50% HPD',
                backgroundColor: 'rgba(103, 235, 114,0.5)',
                borderColor: 'rgba(103, 235, 114, 0.5)'
              },
              {
                data: response.data.hpd_50_upper,
                fill: +3,
                label: 'hide',
                backgroundColor: 'rgba(103, 235, 114,0.5)',
                borderColor: 'rgba(103, 235, 114, 0.5)'
              }
            ]
          }
        this.loaded = true
      } catch (e) {
        console.error(e)
      }
    }
  },
  data: () => ({
    loaded: false,
    chartdata: null,
    chartOptions: null,
    horizon: 365,
    horizons: [
      { text: '7 Days', value: 7 },
      { text: '30 Days', value: 30 },
      { text: '90 Days', value: 90 },
      { text: '365 Days', value: 365 }
    ],
    base: 365,
    bases: [
      { text: '7 Days', value: 7 },
      { text: '30 Days', value: 30 },
      { text: '90 Days', value: 90 },
      { text: '365 Days', value: 365 }
    ],
    vault: null,
    vaults: null
  }),
  async mounted () {
    const response = await axios.get(`${process.env.VUE_APP_API_PROTOCOL}://${process.env.VUE_APP_API_ADDRESS}:${process.env.VUE_APP_API_PORT}/api/vaults`)
    const vaults = response.data.map(x => { return { text: x, value: x } })
    this.vaults = vaults
    this.vault = vaults[0].value
    this.chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        xAxes: [{
          type: 'time',
          time: {
            minUnit: 'day'
          },
          ticks: {
            fontSize: 12
          },
          scaleLabel: {
            display: true,
            fontSize: 12,
            labelString: 'Date'
          }
        }],
        yAxes: [{
          scaleLabel: {
            display: true,
            fontSize: 12,
            labelString: 'PricePerShare'
          }
        }]
      },
      elements: {
        point: {
          radius: 0
        }
      },
      legend: {
        display: true,
        fontSize: 12,
        labels: {
          filter: function (label) {
            if (label.text !== 'hide') return true
          }
        },
        onClick: function (e) {
          e.stopPropagation()
        }
      },
      tooltips: {
        intersect: false,
        mode: 'x',
        itemSort: (a, b) => {
          const aV = a.yLabel
          const bV = b.yLabel
          return (aV < bV) ? 1 : (aV > bV) ? -1 : 0
        },
        callbacks: {
          label: (tooltipItem, data) => {
            const label = tooltipItem.yLabel.toFixed(4)
            return label
          }
        }
      }
    }
    await this.update()
  }
}
</script>
