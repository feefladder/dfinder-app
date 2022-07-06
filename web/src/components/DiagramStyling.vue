<template>
<svg width='0' height='0'>
  <defs>
    <marker id='arrow' markerWidth='10' markerHeight='10' refX='9' refY='3' orient='auto' markerUnits='strokeWidth'>
    <path d='M0,0 L9,3 L0,6' stroke='green' fill='none'/>
    </marker>
    <marker id='unfold_arrow' markerWidth='10' markerHeight='10' refX='0' refY='3' orient='auto' markerUnits='strokeWidth'>
    <path d='M0,3 L9,0 L9,6 z' stroke='green' fill='green' stroke-linejoin='round' />
    </marker>
  </defs>
</svg>
</template>

<style>
.fold-unfold-arrow {
    stroke: green;
    stroke-width: 1;
    marker-start: url(#unfold_arrow);
    marker-end: url(#arrow);
    fill: none;
}

.diagram {
  margin: 10px;
}

.pt_normal {
  stroke: black;
  stroke-width: 1;
}
.pt_hilite {
  stroke: #922;
  stroke-width: 3;
}
.pt_action {
  stroke: #522;
  stroke-width: 3;
}

.l_crease {
  stroke: darkgray;
  stroke-width: .5;
}
.l_edge {
  stroke: #000;
  stroke-width: 2;
}
.l_hilite {
  stroke: darkmagenta;
  stroke-width: 2;
}
.l_valley {
  stroke: green;
  stroke-width: .5;
stroke-dasharray: 2;
}

text {
  fill: #522;
}
</style>
