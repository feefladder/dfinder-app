
const port = location.port
const host = location.hostname


export default {

  baseURL: `${location.protocol}//${host}:${port}`,

  async getDiagrams(divisions) {
      const resp = await fetch(`${this.baseURL}/api/calc-divisions/${divisions}`)
      return await resp.json()
  }
}
  