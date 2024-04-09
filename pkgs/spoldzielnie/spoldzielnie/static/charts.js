

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

