

export function wykres_spoldzielni(name) {
    // Select the body of the document
    let cz = d3.create('svg');
    cz.append('circle')
        .attr('cx', 50)
        .attr('cy', 50)
        .attr('r', 50)
        .style('fill', 'red');

    cz.append('circle')
        .attr('cx', 50)
        .attr('cy', 50)
        .attr('r', 40)
        .style('fill', 'yellow');
    // Append an SVG element to the body
    return cz.node();
}

export function pogrupuj(dane) {
    // const dzielnie = d3.group(dane, (d) => d.dzielnica);
    const dzielnie = d3.rollup(dane, (D) => d3.sum(D, d => d.bilans), (d) => d.dzielnica);
    //sort dzielnie
    const sorted = new Map([...dzielnie.entries()].sort((a, b) => b[1] - a[1]));
    return sorted;
}

export function daj_mi_wykres(dane) {

    //sort dane by value


    // const dzielnie = d3.group(dane, (d) => d.dzielnica);
    let cz = d3.create('svg')
    .attr('width', 460)
    .attr('height', 370)
    .style("background","#fffaaf");
    
    let xscale = d3.scaleLinear()
        .domain([0, d3.max(dane, d => d[1])])
        .range([0, 300]);


    cz.selectAll('rect')
    .data(dane)
    .enter()
    .append('rect')
    .attr('x', 140)
    .attr('y', (d, i) => i * 20+20)
    .attr('width', (d) => xscale(d[1]))
    .attr('height', 10)
    .style('fill', 'red');

    cz.selectAll('text')
    .data(dane)
    .enter()
    .append('text')
    .attr('text-anchor','end')
    .attr('x', 130)
    .attr('y', (d, i) => i * 20+20+10)
    .text((d) => d[0])

    return cz.node();
}
