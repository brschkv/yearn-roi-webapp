<template>
  <div class="home">
    <LineChartContainer/>
  </div>
</template>

<script>
// @ is an alias to /src
import LineChartContainer from '@/components/ChartContainer.vue'

export default {
  name: 'ROI',
  components: {
    LineChartContainer
  }
}
</script>
