export const load = async ({ fetch }) => {
  const fetchContributorsList = async () => {   
    const response = await fetch('https://api.github.com/repos/roll-over/unknown-interview/contributors')
    const result = await response.json()
    return result
  }

  return {
   contributorsList: fetchContributorsList(),
  }
}